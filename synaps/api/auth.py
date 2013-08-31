# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
"""
Common Auth Middleware.

"""

import webob.dec
import webob.exc

from synaps import context
from synaps import flags
from synaps import log as logging
from synaps.openstack.common import cfg
from synaps import wsgi


use_forwarded_for_opt = cfg.BoolOpt('use_forwarded_for',
        default=False,
        help='Treat X-Forwarded-For as the canonical remote address. '
             'Only enable this if you have a sanitizing proxy.')

FLAGS = flags.FLAGS
FLAGS.register_opt(use_forwarded_for_opt)
LOG = logging.getLogger(__name__)


class InjectContext(wsgi.Middleware):
    """Add a 'synaps.context' to WSGI environ."""

    def __init__(self, context, *args, **kwargs):
        self.context = context
        super(InjectContext, self).__init__(*args, **kwargs)

    @webob.dec.wsgify(RequestClass=webob.Request)
    def __call__(self, req):
        req.environ['synaps.context'] = self.context
        return self.application


class SynapsKeystoneContext(wsgi.Middleware):
    """Make a request context from keystone headers"""

    @webob.dec.wsgify(RequestClass=webob.Request)
    def __call__(self, req):
        user_id = req.headers.get('X_USER')
        user_id = req.headers.get('X_USER_ID', user_id)
        if user_id is None:
            LOG.debug("Neither X_USER_ID nor X_USER found in request")
            return webob.exc.HTTPUnauthorized()
        # get the roles
        roles = [r.strip() for r in req.headers.get('X_ROLE', '').split(',')]
        if 'X_TENANT_ID' in req.headers:
            # This is the new header since Keystone went to ID/Name
            project_id = req.headers['X_TENANT_ID']
        else:
            # This is for legacy compatibility
            project_id = req.headers['X_TENANT']

        # Get the auth token
        auth_token = req.headers.get('X_AUTH_TOKEN',
                                     req.headers.get('X_STORAGE_TOKEN'))

        # Build a context, including the auth_token...
        remote_address = req.remote_addr
        if FLAGS.use_forwarded_for:
            remote_address = req.headers.get('X-Forwarded-For', remote_address)
        ctx = context.RequestContext(user_id,
                                     project_id,
                                     roles=roles,
                                     auth_token=auth_token,
                                     strategy='keystone',
                                     remote_address=remote_address)

        req.environ['synaps.context'] = ctx
        return self.application

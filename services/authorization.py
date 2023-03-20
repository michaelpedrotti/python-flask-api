from app import db
from pprint import pprint
from dicts.permission import permission
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.engine.cursor import CursorResult
from sqlalchemy import text


class AuthorizationService():

    def has_permission(self, resource: str = 'user', action: str = 'read', user_id = 0) -> bool:

        action = permission.get(action, action)

        query = "SELECT  \
                COUNT(*) as total \
            FROM user \
            INNER JOIN profile ON(user.profile_id = profile.id) \
            INNER JOIN permission ON(profile.id = permission.profile_id) \
            WHERE user.id = " + str(user_id) + " \
            AND permission.resource = '" + resource + "' \
            AND JSON_CONTAINS(permission.actions, json_quote('" + action + "')) > 0"
        
        session: scoped_session = db.session
        result: CursorResult = session.execute(text(query))
        total, = result.fetchone()
        
        return total > 0

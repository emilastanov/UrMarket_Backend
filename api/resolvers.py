from .models import *

def isAuthenticated(*permission):
    def checkPermisson(func):
        def checkAuth(*args, **kwargs):
            info = args[1]
            req = info.context.headers
            token = req.get('Authorization')
            if not token:
                return {
                    "success": False,
                    "errors": [
                        "Unauthorized"
                    ]
                }
            else:
                user = AuthKey.query.filter(AuthKey.key == token).first()
                if user:
                    if user.permission in permission:
                        return func(*args, **kwargs)
                    else:
                        return {
                            "success": False,
                            "errors": [
                                "Permission denied"
                            ]
                        }
                else:
                    return {
                        "success": False,
                        "errors": [
                            "Unauthorized"
                        ]
                    }

        return checkAuth
    return checkPermisson
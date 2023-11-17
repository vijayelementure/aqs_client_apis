from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException, status, Response


def get_user_token(
    res: Response,
    credential: HTTPAuthorizationCredentials = Depends(
        HTTPBearer(
            auto_error=False,
        )
    ),
):
    if credential is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bearer authentication is needed",
            headers={"WWW-Authenticate": 'Bearer realm="auth_required"'},
        )
    try:
        # decoded_token = auth.verify_id_token(credential.credentials)
        # print(decoded_token)
        pass
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid authentication from Firebase. {err}",
            headers={"WWW-Authenticate": 'Bearer error="invalid_token"'},
        )
    res.headers["WWW-Authenticate"] = 'Bearer realm="auth_required"'
    # return decoded_token
    return None

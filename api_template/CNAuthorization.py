import Exceptions
import Types


def setRightsHolder(session, id, userId, serialVersion):
    """
  ``PUT /owner/{id}`` |br| Changes ownership (RightsHolder) of the specified object to the :term:`subject` specified by `userId`

  v2.0: The supplied identifier may be a :term:`PID` or a :term:`SID`.


  :Version: 1.0, 2.0
  :Use Cases:
    :doc:`UC16 </design/UseCases/16_uc>`
  :REST URL: ``PUT /owner/{id}``

  Parameters:
    session (Types.Session): |session| 
    id (Types.Identifier): Identifier of the object to be modified. May be either a PID or a SID, the latter acting on
      the HEAD PID. Transmitted as part of the URL path and must be escaped accordingly.
    userId (Types.Subject): The subject that will be taking ownership of the specified object. |stringparam|
    serialVersion (unsigned long): The serialVersion of the system metadata that is the intended target for the change. |stringparam|

  Returns:
    Types.Identifier: Identifier of the object that was modified

  Raises:
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4490)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=4480)
    Exceptions.NotAuthorized: The supplied subject does not have permission to change ownership of the object (errorCode=401, detailCode=4440)
    Exceptions.NotFound: The specified object does not exist in the DataONE system (errorCode=404, detailCode=4460)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4441)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=4442)
    Exceptions.VersionMismatch: The serialVersion supplied with the request does not match the serialVersion of the target (errorCode=409, detailCode=4443)

  .. include:: /apis/examples/cnauthorization_setrightsholder.txt

  """
    return None


def isAuthorized(session, id, action):
    """
  ``GET /isAuthorized/{id}?action={action}`` |br| Test if the user identified by the provided token has authorization for operation on the specified object.

  A successful operation is indicated by a return HTTP status of 200.

  Failure is indicated by an exception such as :exc:`NotAuthorized` being returned.

  A successful response is indicated by a response HTTP status of 200. The body of the response is arbitrary and SHOULD
  be ignored by the caller.

  If the action is not authorized, then a :exc:`NotAuthorized` exception MUST be raised.

  v2.0: The supplied identifier may be a :term:`PID` or a :term:`SID`.


  :Version: 1.0, 2.0
  :Use Cases:
    :doc:`UC01 </design/UseCases/01_uc>`, :doc:`UC02 </design/UseCases/02_uc>`, :doc:`UC36 </design/UseCases/36_uc>`, :doc:`UC37 </design/UseCases/37_uc>`
  :REST URL: ``GET /isAuthorized/{id}?action={action}``

  Parameters:
    session (Types.Session): |session| 
    id (Types.Identifier): The identifer of the resource for which access is being checked. May be either a PID or a
      SID, the latter returning results as if called with the HEAD PID. Transmitted as part of the URL path and must be escaped accordingly.
    action (Types.Permission): The type of operation which is being requested for the given identifier. |urlparam|

  Returns:
    boolean: True if the operation is allowed

  Raises:
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=1760)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=1840)
    Exceptions.NotFound:  (errorCode=404, detailCode=1800)
    Exceptions.NotAuthorized: This error is raised if the request comes from a black listed source (e.g. a temporary
      block may be imposed on a source that calls this method too many times within some time interval) (errorCode=401, detailCode=1820)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=1780)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=1761)

  .. include:: /apis/examples/cnauthorization_isauthorized.txt

  """
    return None


def setAccessPolicy(session, id, accessPolicy, serialVersion):
    """
  ``PUT /accessRules/{id}`` |br| Sets the access permissions for an object identified by *id*.

  Triggers a change to the system metadata modified time stamp.

  Successful completion of this operation is indicated by a HTTP response status code of 200.

  Unsuccessful completion of this operation MUST be indicated by returning an appropriate exception such as :exc:`NotAuthorized`.

  v2.0: The supplied identifier may be a :term:`PID` or a :term:`SID`.


  :Version: 1.0, 2.0
  :Use Cases:
    :doc:`UC16 </design/UseCases/16_uc>`
  :REST URL: ``PUT /accessRules/{id}``

  Parameters:
    session (Types.Session): |session| 
    id (Types.Identifier): The object for which access control is being updated. May be either a PID or a SID, the
      latter acting on the HEAD PID only. |urlparam|
    accessPolicy (Types.AccessPolicy): The desired privileges to be assigned to the object. |xmlparam|
    serialVersion (unsigned long): The serialVersion of the system metadata that is the intended target for the change. |stringparam|

  Returns:
    boolean: True if the operation succeeds, otherwise false.

  Raises:
    Exceptions.InvalidToken: The supplied token is invalid (errorCode=401, detailCode=4410)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4430)
    Exceptions.NotFound: The specified object does not exist in the DataONE system (errorCode=404, detailCode=4400)
    Exceptions.NotAuthorized: The :term:`Subject` does not have permission to alter access control rules for the object. (errorCode=401, detailCode=4420)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4401)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=4402)
    Exceptions.VersionMismatch: The serialVersion supplied with the request does not match the serialVersion of the target (errorCode=409, detailCode=4403)

  .. include:: /apis/examples/cnauthorization_setaccesspolicy.txt

  """
    return None

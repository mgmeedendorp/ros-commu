; Auto-generated. Do not edit!


(cl:in-package commu_wrapper-srv)


;//! \htmlinclude CommULook-request.msg.html

(cl:defclass <CommULook-request> (roslisp-msg-protocol:ros-message)
  ((camera_info
    :reader camera_info
    :initarg :camera_info
    :type sensor_msgs-msg:CameraInfo
    :initform (cl:make-instance 'sensor_msgs-msg:CameraInfo))
   (camera_transform
    :reader camera_transform
    :initarg :camera_transform
    :type geometry_msgs-msg:Transform
    :initform (cl:make-instance 'geometry_msgs-msg:Transform))
   (look_x
    :reader look_x
    :initarg :look_x
    :type cl:fixnum
    :initform 0)
   (look_y
    :reader look_y
    :initarg :look_y
    :type cl:fixnum
    :initform 0))
)

(cl:defclass CommULook-request (<CommULook-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CommULook-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CommULook-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name commu_wrapper-srv:<CommULook-request> is deprecated: use commu_wrapper-srv:CommULook-request instead.")))

(cl:ensure-generic-function 'camera_info-val :lambda-list '(m))
(cl:defmethod camera_info-val ((m <CommULook-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader commu_wrapper-srv:camera_info-val is deprecated.  Use commu_wrapper-srv:camera_info instead.")
  (camera_info m))

(cl:ensure-generic-function 'camera_transform-val :lambda-list '(m))
(cl:defmethod camera_transform-val ((m <CommULook-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader commu_wrapper-srv:camera_transform-val is deprecated.  Use commu_wrapper-srv:camera_transform instead.")
  (camera_transform m))

(cl:ensure-generic-function 'look_x-val :lambda-list '(m))
(cl:defmethod look_x-val ((m <CommULook-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader commu_wrapper-srv:look_x-val is deprecated.  Use commu_wrapper-srv:look_x instead.")
  (look_x m))

(cl:ensure-generic-function 'look_y-val :lambda-list '(m))
(cl:defmethod look_y-val ((m <CommULook-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader commu_wrapper-srv:look_y-val is deprecated.  Use commu_wrapper-srv:look_y instead.")
  (look_y m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CommULook-request>) ostream)
  "Serializes a message object of type '<CommULook-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'camera_info) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'camera_transform) ostream)
  (cl:let* ((signed (cl:slot-value msg 'look_x)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'look_y)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CommULook-request>) istream)
  "Deserializes a message object of type '<CommULook-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'camera_info) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'camera_transform) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'look_x) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'look_y) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CommULook-request>)))
  "Returns string type for a service object of type '<CommULook-request>"
  "commu_wrapper/CommULookRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CommULook-request)))
  "Returns string type for a service object of type 'CommULook-request"
  "commu_wrapper/CommULookRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CommULook-request>)))
  "Returns md5sum for a message object of type '<CommULook-request>"
  "f140a05a390d4967a567a474c5dfde3f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CommULook-request)))
  "Returns md5sum for a message object of type 'CommULook-request"
  "f140a05a390d4967a567a474c5dfde3f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CommULook-request>)))
  "Returns full string definition for message of type '<CommULook-request>"
  (cl:format cl:nil "~%~%~%~%~%sensor_msgs/CameraInfo camera_info~%~%~%geometry_msgs/Transform camera_transform~%~%~%int8 look_x~%int8 look_y~%~%~%================================================================================~%MSG: sensor_msgs/CameraInfo~%# This message defines meta information for a camera. It should be in a~%# camera namespace on topic \"camera_info\" and accompanied by up to five~%# image topics named:~%#~%#   image_raw - raw data from the camera driver, possibly Bayer encoded~%#   image            - monochrome, distorted~%#   image_color      - color, distorted~%#   image_rect       - monochrome, rectified~%#   image_rect_color - color, rectified~%#~%# The image_pipeline contains packages (image_proc, stereo_image_proc)~%# for producing the four processed image topics from image_raw and~%# camera_info. The meaning of the camera parameters are described in~%# detail at http://www.ros.org/wiki/image_pipeline/CameraInfo.~%#~%# The image_geometry package provides a user-friendly interface to~%# common operations using this meta information. If you want to, e.g.,~%# project a 3d point into image coordinates, we strongly recommend~%# using image_geometry.~%#~%# If the camera is uncalibrated, the matrices D, K, R, P should be left~%# zeroed out. In particular, clients may assume that K[0] == 0.0~%# indicates an uncalibrated camera.~%~%#######################################################################~%#                     Image acquisition info                          #~%#######################################################################~%~%# Time of image acquisition, camera coordinate frame ID~%Header header    # Header timestamp should be acquisition time of image~%                 # Header frame_id should be optical frame of camera~%                 # origin of frame should be optical center of camera~%                 # +x should point to the right in the image~%                 # +y should point down in the image~%                 # +z should point into the plane of the image~%~%~%#######################################################################~%#                      Calibration Parameters                         #~%#######################################################################~%# These are fixed during camera calibration. Their values will be the #~%# same in all messages until the camera is recalibrated. Note that    #~%# self-calibrating systems may \"recalibrate\" frequently.              #~%#                                                                     #~%# The internal parameters can be used to warp a raw (distorted) image #~%# to:                                                                 #~%#   1. An undistorted image (requires D and K)                        #~%#   2. A rectified image (requires D, K, R)                           #~%# The projection matrix P projects 3D points into the rectified image.#~%#######################################################################~%~%# The image dimensions with which the camera was calibrated. Normally~%# this will be the full camera resolution in pixels.~%uint32 height~%uint32 width~%~%# The distortion model used. Supported models are listed in~%# sensor_msgs/distortion_models.h. For most cameras, \"plumb_bob\" - a~%# simple model of radial and tangential distortion - is sufficient.~%string distortion_model~%~%# The distortion parameters, size depending on the distortion model.~%# For \"plumb_bob\", the 5 parameters are: (k1, k2, t1, t2, k3).~%float64[] D~%~%# Intrinsic camera matrix for the raw (distorted) images.~%#     [fx  0 cx]~%# K = [ 0 fy cy]~%#     [ 0  0  1]~%# Projects 3D points in the camera coordinate frame to 2D pixel~%# coordinates using the focal lengths (fx, fy) and principal point~%# (cx, cy).~%float64[9]  K # 3x3 row-major matrix~%~%# Rectification matrix (stereo cameras only)~%# A rotation matrix aligning the camera coordinate system to the ideal~%# stereo image plane so that epipolar lines in both stereo images are~%# parallel.~%float64[9]  R # 3x3 row-major matrix~%~%# Projection/camera matrix~%#     [fx'  0  cx' Tx]~%# P = [ 0  fy' cy' Ty]~%#     [ 0   0   1   0]~%# By convention, this matrix specifies the intrinsic (camera) matrix~%#  of the processed (rectified) image. That is, the left 3x3 portion~%#  is the normal camera intrinsic matrix for the rectified image.~%# It projects 3D points in the camera coordinate frame to 2D pixel~%#  coordinates using the focal lengths (fx', fy') and principal point~%#  (cx', cy') - these may differ from the values in K.~%# For monocular cameras, Tx = Ty = 0. Normally, monocular cameras will~%#  also have R = the identity and P[1:3,1:3] = K.~%# For a stereo pair, the fourth column [Tx Ty 0]' is related to the~%#  position of the optical center of the second camera in the first~%#  camera's frame. We assume Tz = 0 so both cameras are in the same~%#  stereo image plane. The first camera always has Tx = Ty = 0. For~%#  the right (second) camera of a horizontal stereo pair, Ty = 0 and~%#  Tx = -fx' * B, where B is the baseline between the cameras.~%# Given a 3D point [X Y Z]', the projection (x, y) of the point onto~%#  the rectified image is given by:~%#  [u v w]' = P * [X Y Z 1]'~%#         x = u / w~%#         y = v / w~%#  This holds for both images of a stereo pair.~%float64[12] P # 3x4 row-major matrix~%~%~%#######################################################################~%#                      Operational Parameters                         #~%#######################################################################~%# These define the image region actually captured by the camera       #~%# driver. Although they affect the geometry of the output image, they #~%# may be changed freely without recalibrating the camera.             #~%#######################################################################~%~%# Binning refers here to any camera setting which combines rectangular~%#  neighborhoods of pixels into larger \"super-pixels.\" It reduces the~%#  resolution of the output image to~%#  (width / binning_x) x (height / binning_y).~%# The default values binning_x = binning_y = 0 is considered the same~%#  as binning_x = binning_y = 1 (no subsampling).~%uint32 binning_x~%uint32 binning_y~%~%# Region of interest (subwindow of full camera resolution), given in~%#  full resolution (unbinned) image coordinates. A particular ROI~%#  always denotes the same window of pixels on the camera sensor,~%#  regardless of binning settings.~%# The default setting of roi (all values 0) is considered the same as~%#  full resolution (roi.width = width, roi.height = height).~%RegionOfInterest roi~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: sensor_msgs/RegionOfInterest~%# This message is used to specify a region of interest within an image.~%#~%# When used to specify the ROI setting of the camera when the image was~%# taken, the height and width fields should either match the height and~%# width fields for the associated image; or height = width = 0~%# indicates that the full resolution image was captured.~%~%uint32 x_offset  # Leftmost pixel of the ROI~%                 # (0 if the ROI includes the left edge of the image)~%uint32 y_offset  # Topmost pixel of the ROI~%                 # (0 if the ROI includes the top edge of the image)~%uint32 height    # Height of ROI~%uint32 width     # Width of ROI~%~%# True if a distinct rectified ROI should be calculated from the \"raw\"~%# ROI in this message. Typically this should be False if the full image~%# is captured (ROI not used), and True if a subwindow is captured (ROI~%# used).~%bool do_rectify~%~%================================================================================~%MSG: geometry_msgs/Transform~%# This represents the transform between two coordinate frames in free space.~%~%Vector3 translation~%Quaternion rotation~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CommULook-request)))
  "Returns full string definition for message of type 'CommULook-request"
  (cl:format cl:nil "~%~%~%~%~%sensor_msgs/CameraInfo camera_info~%~%~%geometry_msgs/Transform camera_transform~%~%~%int8 look_x~%int8 look_y~%~%~%================================================================================~%MSG: sensor_msgs/CameraInfo~%# This message defines meta information for a camera. It should be in a~%# camera namespace on topic \"camera_info\" and accompanied by up to five~%# image topics named:~%#~%#   image_raw - raw data from the camera driver, possibly Bayer encoded~%#   image            - monochrome, distorted~%#   image_color      - color, distorted~%#   image_rect       - monochrome, rectified~%#   image_rect_color - color, rectified~%#~%# The image_pipeline contains packages (image_proc, stereo_image_proc)~%# for producing the four processed image topics from image_raw and~%# camera_info. The meaning of the camera parameters are described in~%# detail at http://www.ros.org/wiki/image_pipeline/CameraInfo.~%#~%# The image_geometry package provides a user-friendly interface to~%# common operations using this meta information. If you want to, e.g.,~%# project a 3d point into image coordinates, we strongly recommend~%# using image_geometry.~%#~%# If the camera is uncalibrated, the matrices D, K, R, P should be left~%# zeroed out. In particular, clients may assume that K[0] == 0.0~%# indicates an uncalibrated camera.~%~%#######################################################################~%#                     Image acquisition info                          #~%#######################################################################~%~%# Time of image acquisition, camera coordinate frame ID~%Header header    # Header timestamp should be acquisition time of image~%                 # Header frame_id should be optical frame of camera~%                 # origin of frame should be optical center of camera~%                 # +x should point to the right in the image~%                 # +y should point down in the image~%                 # +z should point into the plane of the image~%~%~%#######################################################################~%#                      Calibration Parameters                         #~%#######################################################################~%# These are fixed during camera calibration. Their values will be the #~%# same in all messages until the camera is recalibrated. Note that    #~%# self-calibrating systems may \"recalibrate\" frequently.              #~%#                                                                     #~%# The internal parameters can be used to warp a raw (distorted) image #~%# to:                                                                 #~%#   1. An undistorted image (requires D and K)                        #~%#   2. A rectified image (requires D, K, R)                           #~%# The projection matrix P projects 3D points into the rectified image.#~%#######################################################################~%~%# The image dimensions with which the camera was calibrated. Normally~%# this will be the full camera resolution in pixels.~%uint32 height~%uint32 width~%~%# The distortion model used. Supported models are listed in~%# sensor_msgs/distortion_models.h. For most cameras, \"plumb_bob\" - a~%# simple model of radial and tangential distortion - is sufficient.~%string distortion_model~%~%# The distortion parameters, size depending on the distortion model.~%# For \"plumb_bob\", the 5 parameters are: (k1, k2, t1, t2, k3).~%float64[] D~%~%# Intrinsic camera matrix for the raw (distorted) images.~%#     [fx  0 cx]~%# K = [ 0 fy cy]~%#     [ 0  0  1]~%# Projects 3D points in the camera coordinate frame to 2D pixel~%# coordinates using the focal lengths (fx, fy) and principal point~%# (cx, cy).~%float64[9]  K # 3x3 row-major matrix~%~%# Rectification matrix (stereo cameras only)~%# A rotation matrix aligning the camera coordinate system to the ideal~%# stereo image plane so that epipolar lines in both stereo images are~%# parallel.~%float64[9]  R # 3x3 row-major matrix~%~%# Projection/camera matrix~%#     [fx'  0  cx' Tx]~%# P = [ 0  fy' cy' Ty]~%#     [ 0   0   1   0]~%# By convention, this matrix specifies the intrinsic (camera) matrix~%#  of the processed (rectified) image. That is, the left 3x3 portion~%#  is the normal camera intrinsic matrix for the rectified image.~%# It projects 3D points in the camera coordinate frame to 2D pixel~%#  coordinates using the focal lengths (fx', fy') and principal point~%#  (cx', cy') - these may differ from the values in K.~%# For monocular cameras, Tx = Ty = 0. Normally, monocular cameras will~%#  also have R = the identity and P[1:3,1:3] = K.~%# For a stereo pair, the fourth column [Tx Ty 0]' is related to the~%#  position of the optical center of the second camera in the first~%#  camera's frame. We assume Tz = 0 so both cameras are in the same~%#  stereo image plane. The first camera always has Tx = Ty = 0. For~%#  the right (second) camera of a horizontal stereo pair, Ty = 0 and~%#  Tx = -fx' * B, where B is the baseline between the cameras.~%# Given a 3D point [X Y Z]', the projection (x, y) of the point onto~%#  the rectified image is given by:~%#  [u v w]' = P * [X Y Z 1]'~%#         x = u / w~%#         y = v / w~%#  This holds for both images of a stereo pair.~%float64[12] P # 3x4 row-major matrix~%~%~%#######################################################################~%#                      Operational Parameters                         #~%#######################################################################~%# These define the image region actually captured by the camera       #~%# driver. Although they affect the geometry of the output image, they #~%# may be changed freely without recalibrating the camera.             #~%#######################################################################~%~%# Binning refers here to any camera setting which combines rectangular~%#  neighborhoods of pixels into larger \"super-pixels.\" It reduces the~%#  resolution of the output image to~%#  (width / binning_x) x (height / binning_y).~%# The default values binning_x = binning_y = 0 is considered the same~%#  as binning_x = binning_y = 1 (no subsampling).~%uint32 binning_x~%uint32 binning_y~%~%# Region of interest (subwindow of full camera resolution), given in~%#  full resolution (unbinned) image coordinates. A particular ROI~%#  always denotes the same window of pixels on the camera sensor,~%#  regardless of binning settings.~%# The default setting of roi (all values 0) is considered the same as~%#  full resolution (roi.width = width, roi.height = height).~%RegionOfInterest roi~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: sensor_msgs/RegionOfInterest~%# This message is used to specify a region of interest within an image.~%#~%# When used to specify the ROI setting of the camera when the image was~%# taken, the height and width fields should either match the height and~%# width fields for the associated image; or height = width = 0~%# indicates that the full resolution image was captured.~%~%uint32 x_offset  # Leftmost pixel of the ROI~%                 # (0 if the ROI includes the left edge of the image)~%uint32 y_offset  # Topmost pixel of the ROI~%                 # (0 if the ROI includes the top edge of the image)~%uint32 height    # Height of ROI~%uint32 width     # Width of ROI~%~%# True if a distinct rectified ROI should be calculated from the \"raw\"~%# ROI in this message. Typically this should be False if the full image~%# is captured (ROI not used), and True if a subwindow is captured (ROI~%# used).~%bool do_rectify~%~%================================================================================~%MSG: geometry_msgs/Transform~%# This represents the transform between two coordinate frames in free space.~%~%Vector3 translation~%Quaternion rotation~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CommULook-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'camera_info))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'camera_transform))
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CommULook-request>))
  "Converts a ROS message object to a list"
  (cl:list 'CommULook-request
    (cl:cons ':camera_info (camera_info msg))
    (cl:cons ':camera_transform (camera_transform msg))
    (cl:cons ':look_x (look_x msg))
    (cl:cons ':look_y (look_y msg))
))
;//! \htmlinclude CommULook-response.msg.html

(cl:defclass <CommULook-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass CommULook-response (<CommULook-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CommULook-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CommULook-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name commu_wrapper-srv:<CommULook-response> is deprecated: use commu_wrapper-srv:CommULook-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <CommULook-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader commu_wrapper-srv:success-val is deprecated.  Use commu_wrapper-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CommULook-response>) ostream)
  "Serializes a message object of type '<CommULook-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CommULook-response>) istream)
  "Deserializes a message object of type '<CommULook-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CommULook-response>)))
  "Returns string type for a service object of type '<CommULook-response>"
  "commu_wrapper/CommULookResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CommULook-response)))
  "Returns string type for a service object of type 'CommULook-response"
  "commu_wrapper/CommULookResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CommULook-response>)))
  "Returns md5sum for a message object of type '<CommULook-response>"
  "f140a05a390d4967a567a474c5dfde3f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CommULook-response)))
  "Returns md5sum for a message object of type 'CommULook-response"
  "f140a05a390d4967a567a474c5dfde3f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CommULook-response>)))
  "Returns full string definition for message of type '<CommULook-response>"
  (cl:format cl:nil "~%~%bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CommULook-response)))
  "Returns full string definition for message of type 'CommULook-response"
  (cl:format cl:nil "~%~%bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CommULook-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CommULook-response>))
  "Converts a ROS message object to a list"
  (cl:list 'CommULook-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'CommULook)))
  'CommULook-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'CommULook)))
  'CommULook-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CommULook)))
  "Returns string type for a service object of type '<CommULook>"
  "commu_wrapper/CommULook")
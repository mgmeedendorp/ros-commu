// Auto-generated. Do not edit!

// (in-package look_helper.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class SetLookAtTargetRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.target_frame_name = null;
    }
    else {
      if (initObj.hasOwnProperty('target_frame_name')) {
        this.target_frame_name = initObj.target_frame_name
      }
      else {
        this.target_frame_name = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SetLookAtTargetRequest
    // Serialize message field [target_frame_name]
    bufferOffset = _serializer.string(obj.target_frame_name, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SetLookAtTargetRequest
    let len;
    let data = new SetLookAtTargetRequest(null);
    // Deserialize message field [target_frame_name]
    data.target_frame_name = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.target_frame_name.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'look_helper/SetLookAtTargetRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'f035c613d0c3285d785da141558423bb';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    
    
    string target_frame_name
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SetLookAtTargetRequest(null);
    if (msg.target_frame_name !== undefined) {
      resolved.target_frame_name = msg.target_frame_name;
    }
    else {
      resolved.target_frame_name = ''
    }

    return resolved;
    }
};

class SetLookAtTargetResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.success = null;
    }
    else {
      if (initObj.hasOwnProperty('success')) {
        this.success = initObj.success
      }
      else {
        this.success = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SetLookAtTargetResponse
    // Serialize message field [success]
    bufferOffset = _serializer.bool(obj.success, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SetLookAtTargetResponse
    let len;
    let data = new SetLookAtTargetResponse(null);
    // Deserialize message field [success]
    data.success = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'look_helper/SetLookAtTargetResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '358e233cde0c8a8bcfea4ce193f8fc15';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    
    bool success
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SetLookAtTargetResponse(null);
    if (msg.success !== undefined) {
      resolved.success = msg.success;
    }
    else {
      resolved.success = false
    }

    return resolved;
    }
};

module.exports = {
  Request: SetLookAtTargetRequest,
  Response: SetLookAtTargetResponse,
  md5sum() { return '1030478efebc9e6deae2c1ba1ffff144'; },
  datatype() { return 'look_helper/SetLookAtTarget'; }
};

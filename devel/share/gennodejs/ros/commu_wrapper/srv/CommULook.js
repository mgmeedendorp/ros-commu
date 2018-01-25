// Auto-generated. Do not edit!

// (in-package commu_wrapper.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class CommULookRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.look_x = null;
      this.look_y = null;
      this.look_z = null;
    }
    else {
      if (initObj.hasOwnProperty('look_x')) {
        this.look_x = initObj.look_x
      }
      else {
        this.look_x = 0;
      }
      if (initObj.hasOwnProperty('look_y')) {
        this.look_y = initObj.look_y
      }
      else {
        this.look_y = 0;
      }
      if (initObj.hasOwnProperty('look_z')) {
        this.look_z = initObj.look_z
      }
      else {
        this.look_z = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type CommULookRequest
    // Serialize message field [look_x]
    bufferOffset = _serializer.int32(obj.look_x, buffer, bufferOffset);
    // Serialize message field [look_y]
    bufferOffset = _serializer.int32(obj.look_y, buffer, bufferOffset);
    // Serialize message field [look_z]
    bufferOffset = _serializer.int32(obj.look_z, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type CommULookRequest
    let len;
    let data = new CommULookRequest(null);
    // Deserialize message field [look_x]
    data.look_x = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [look_y]
    data.look_y = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [look_z]
    data.look_z = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 12;
  }

  static datatype() {
    // Returns string type for a service object
    return 'commu_wrapper/CommULookRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '933be4a7ef5344e40fff306ee2eddba8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    
    
    
    int32 look_x
    
    
    int32 look_y
    
    
    int32 look_z
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new CommULookRequest(null);
    if (msg.look_x !== undefined) {
      resolved.look_x = msg.look_x;
    }
    else {
      resolved.look_x = 0
    }

    if (msg.look_y !== undefined) {
      resolved.look_y = msg.look_y;
    }
    else {
      resolved.look_y = 0
    }

    if (msg.look_z !== undefined) {
      resolved.look_z = msg.look_z;
    }
    else {
      resolved.look_z = 0
    }

    return resolved;
    }
};

class CommULookResponse {
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
    // Serializes a message object of type CommULookResponse
    // Serialize message field [success]
    bufferOffset = _serializer.bool(obj.success, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type CommULookResponse
    let len;
    let data = new CommULookResponse(null);
    // Deserialize message field [success]
    data.success = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'commu_wrapper/CommULookResponse';
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
    const resolved = new CommULookResponse(null);
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
  Request: CommULookRequest,
  Response: CommULookResponse,
  md5sum() { return '586b9328c974a82a91e07618b791be94'; },
  datatype() { return 'commu_wrapper/CommULook'; }
};

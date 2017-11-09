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

class CommUUtterRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.utterance = null;
      this.blocking = null;
      this.english = null;
    }
    else {
      if (initObj.hasOwnProperty('utterance')) {
        this.utterance = initObj.utterance
      }
      else {
        this.utterance = '';
      }
      if (initObj.hasOwnProperty('blocking')) {
        this.blocking = initObj.blocking
      }
      else {
        this.blocking = false;
      }
      if (initObj.hasOwnProperty('english')) {
        this.english = initObj.english
      }
      else {
        this.english = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type CommUUtterRequest
    // Serialize message field [utterance]
    bufferOffset = _serializer.string(obj.utterance, buffer, bufferOffset);
    // Serialize message field [blocking]
    bufferOffset = _serializer.bool(obj.blocking, buffer, bufferOffset);
    // Serialize message field [english]
    bufferOffset = _serializer.bool(obj.english, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type CommUUtterRequest
    let len;
    let data = new CommUUtterRequest(null);
    // Deserialize message field [utterance]
    data.utterance = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [blocking]
    data.blocking = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [english]
    data.english = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.utterance.length;
    return length + 6;
  }

  static datatype() {
    // Returns string type for a service object
    return 'commu_wrapper/CommUUtterRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '2afd6b4bdd4b8c861ea7fc877665051d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    string utterance
    
    
    
    bool blocking
    
    
    
    bool english
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new CommUUtterRequest(null);
    if (msg.utterance !== undefined) {
      resolved.utterance = msg.utterance;
    }
    else {
      resolved.utterance = ''
    }

    if (msg.blocking !== undefined) {
      resolved.blocking = msg.blocking;
    }
    else {
      resolved.blocking = false
    }

    if (msg.english !== undefined) {
      resolved.english = msg.english;
    }
    else {
      resolved.english = false
    }

    return resolved;
    }
};

class CommUUtterResponse {
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
    // Serializes a message object of type CommUUtterResponse
    // Serialize message field [success]
    bufferOffset = _serializer.bool(obj.success, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type CommUUtterResponse
    let len;
    let data = new CommUUtterResponse(null);
    // Deserialize message field [success]
    data.success = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'commu_wrapper/CommUUtterResponse';
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
    const resolved = new CommUUtterResponse(null);
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
  Request: CommUUtterRequest,
  Response: CommUUtterResponse,
  md5sum() { return 'fc4efb8806f0415eaa9b069b92459024'; },
  datatype() { return 'commu_wrapper/CommUUtter'; }
};

// Auto-generated. Do not edit!

// (in-package commu_helper.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class BoundingBox {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.x_min = null;
      this.y_min = null;
      this.x_size = null;
      this.y_size = null;
    }
    else {
      if (initObj.hasOwnProperty('x_min')) {
        this.x_min = initObj.x_min
      }
      else {
        this.x_min = 0.0;
      }
      if (initObj.hasOwnProperty('y_min')) {
        this.y_min = initObj.y_min
      }
      else {
        this.y_min = 0.0;
      }
      if (initObj.hasOwnProperty('x_size')) {
        this.x_size = initObj.x_size
      }
      else {
        this.x_size = 0.0;
      }
      if (initObj.hasOwnProperty('y_size')) {
        this.y_size = initObj.y_size
      }
      else {
        this.y_size = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type BoundingBox
    // Serialize message field [x_min]
    bufferOffset = _serializer.float64(obj.x_min, buffer, bufferOffset);
    // Serialize message field [y_min]
    bufferOffset = _serializer.float64(obj.y_min, buffer, bufferOffset);
    // Serialize message field [x_size]
    bufferOffset = _serializer.float64(obj.x_size, buffer, bufferOffset);
    // Serialize message field [y_size]
    bufferOffset = _serializer.float64(obj.y_size, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type BoundingBox
    let len;
    let data = new BoundingBox(null);
    // Deserialize message field [x_min]
    data.x_min = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [y_min]
    data.y_min = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [x_size]
    data.x_size = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [y_size]
    data.y_size = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 32;
  }

  static datatype() {
    // Returns string type for a message object
    return 'commu_helper/BoundingBox';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '49841939163c4125050016679dd0cb15';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # A simple 2d bounding box message
    
    float64 x_min
    float64 y_min
    float64 x_size
    float64 y_size
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new BoundingBox(null);
    if (msg.x_min !== undefined) {
      resolved.x_min = msg.x_min;
    }
    else {
      resolved.x_min = 0.0
    }

    if (msg.y_min !== undefined) {
      resolved.y_min = msg.y_min;
    }
    else {
      resolved.y_min = 0.0
    }

    if (msg.x_size !== undefined) {
      resolved.x_size = msg.x_size;
    }
    else {
      resolved.x_size = 0.0
    }

    if (msg.y_size !== undefined) {
      resolved.y_size = msg.y_size;
    }
    else {
      resolved.y_size = 0.0
    }

    return resolved;
    }
};

module.exports = BoundingBox;

# A message representing an object that was classified using caffe.
Header header

# The certainty of the classification from 0 to 1
float64 score

# The label attached to this object
string label

# The id of this object. This is only unique for one classification forom one image.
string id

# The bounding box for the classified object
BoundingBox bbox
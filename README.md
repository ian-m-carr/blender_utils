# blender_utils

A dumping ground for any useful blender extensions.

## Object distribute along axes

Currently contains an Object context menu extension which will distribute the selected object uniformly along a filterable set of axes.

The first point is the location of the active object, the last point is the location of the object furthest away from the active object along the selected global axes.
The remaining objects are moved to lie on a line between these two points, and the spacing between their origins is an equal division of the length of the line. 

The order of the resulting objects depends on their distance from the active object along the selected axes, To get the results you expect, it's best to have the object roughly in the correct positions (distances from the active object) before applying the operation!

example:

![image](https://github.com/ian-m-carr/blender_utils/assets/7975054/9192ced0-63d8-4daa-b4f6-ec14aeb3aaaa)

cone is active object sphere is furthest away from cone

![image](https://github.com/ian-m-carr/blender_utils/assets/7975054/1dd5e94a-a06c-4895-b854-fab814fd48ea)

distributing in x,y and z

![image](https://github.com/ian-m-carr/blender_utils/assets/7975054/14d30488-0821-4552-a011-9c56c9a202ad)

but if we activate one of the cubes

![image](https://github.com/ian-m-carr/blender_utils/assets/7975054/8c9cd7f8-f867-40f4-947d-b67a9620b988)

The cone is reordered to fit based on the distances from the cube

![image](https://github.com/ian-m-carr/blender_utils/assets/7975054/39450fb2-5513-4118-86cd-6545ea48526e)

selecting only one (or two) of the axes distributes only along those axes

![image](https://github.com/ian-m-carr/blender_utils/assets/7975054/be64c28d-aef6-4692-9d68-0cf6c3018f2d)

![image](https://github.com/ian-m-carr/blender_utils/assets/7975054/efd852cf-0248-4187-a93c-40eafda47e51)

## Outliner tools by APEC

Added these useful additions for selecting and duplicating in the outliner, file is original, 
added here to get auto registration at startup
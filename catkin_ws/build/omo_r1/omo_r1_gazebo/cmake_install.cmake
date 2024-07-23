# Install script for directory: /home/cgvlab/catkin_ws/src/omo_r1/omo_r1_gazebo

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/cgvlab/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/cgvlab/catkin_ws/build/omo_r1/omo_r1_gazebo/catkin_generated/installspace/omo_r1_gazebo.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/omo_r1_gazebo/cmake" TYPE FILE FILES
    "/home/cgvlab/catkin_ws/build/omo_r1/omo_r1_gazebo/catkin_generated/installspace/omo_r1_gazeboConfig.cmake"
    "/home/cgvlab/catkin_ws/build/omo_r1/omo_r1_gazebo/catkin_generated/installspace/omo_r1_gazeboConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/omo_r1_gazebo" TYPE FILE FILES "/home/cgvlab/catkin_ws/src/omo_r1/omo_r1_gazebo/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/omo_r1_gazebo" TYPE DIRECTORY FILES
    "/home/cgvlab/catkin_ws/src/omo_r1/omo_r1_gazebo/launch"
    "/home/cgvlab/catkin_ws/src/omo_r1/omo_r1_gazebo/models"
    "/home/cgvlab/catkin_ws/src/omo_r1/omo_r1_gazebo/rviz"
    "/home/cgvlab/catkin_ws/src/omo_r1/omo_r1_gazebo/sdf"
    "/home/cgvlab/catkin_ws/src/omo_r1/omo_r1_gazebo/worlds"
    )
endif()


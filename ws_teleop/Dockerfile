# docker build -t my_image .

FROM osrf/ros:humble-desktop-full


# Install my programs and utilities
RUN apt-get update \
    && apt-get install -y \
    nano \
    iputils-ping \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

# Install Gazebo
RUN apt-get update \
    && apt-get install -y \
    ros-humble-gazebo-ros-pkgs \
    ros-humble-gazebo-ros2-control \
    && rm -rf /var/lib/apt/lists/*

# Make sure that xacro and joint_state_publisher_gui are installed
RUN apt-get update \
    && apt-get install -y \
    ros-humble-xacro \
    ros-humble-joint-state-publisher-gui \
    && rm -rf /var/lib/apt/lists/*

# Install ROS2 Control
RUN apt-get update \
    && apt-get install -y \
    libusb-1.0-0-dev \
    ros-humble-ros2-control \
    ros-humble-ros2-controllers \
    && rm -rf /var/lib/apt/lists/*


# Install TWIST MUX toolbox
RUN apt-get update \
    && apt-get install -y \
    ros-humble-twist-mux \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user
ARG USERNAME=zp
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
  && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
  && mkdir /home/$USERNAME/.config && chown $USER_UID:$USER_GID /home/$USERNAME/.config


# Set up sudo
RUN apt-get update \
  && apt-get install -y sudo \
  && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME\
  && chmod 0440 /etc/sudoers.d/$USERNAME \
  && rm -rf /var/lib/apt/lists/*


# Copy the entrypoint and bashrc scripts so we have 
# our container's environment set up correctly
COPY entrypoint.sh /entrypoint.sh
COPY bashrc /home/${USERNAME}/.bashrc

# Copy Gazebo model files
#COPY description/ /home/${USERNAME}/.gazebo/models/zbot/

# Set up entrypoint and default command
#ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
#CMD ["bash"]

ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
CMD ["bash"]

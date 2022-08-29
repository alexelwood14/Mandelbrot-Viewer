# Alex Elwood | June 2020

import glfw
import math
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy


# Generates all rendering presets and performs OpenGL rendering setup functions
def initiate(resolution, fullscreen, double):

    glfw.init()
    data_size = 4
    line_length = 2

    # Opens a windowed GLFW window
    if fullscreen:
        window = glfw.create_window(resolution[0], resolution[1], "Mandelbrot Set", glfw.get_primary_monitor(), None)
    else:
        window = glfw.create_window(resolution[0], resolution[1], "Mandelbrot Set", None, None)

    # OpenGL and GLFW presets and shader initiation
    glfw.make_context_current(window)
    shader = create_shader(double)
    glEnable(GL_DEPTH_TEST)
    glClearColor(0, 0, 1.0, 1.0)

    # Initiates all shader uniforms and places their access locations in a dictionary

    # Presets all constant shader uniforms
    render_data = {"shader": shader,
                   "window": window,
                   "data_size": data_size,
                   "line_length": line_length}

    return render_data


def read_shader(filename):
    with open('shaders/'+filename) as f:
        shader = f.read()
    return shader

# Defines the shaders and passes them OpenGL on the GPU
def create_shader(double):

    # Defines the vertex shader including its uniforms and functions
    vertex_shader = read_shader('vertex.glsl')

    # Defines the fragment shader including its uniforms and functions
    if double:
        fragment_shader = read_shader('double-fragment.glsl')
    else:
        fragment_shader = read_shader('single-fragment.glsl')

    # Compile the shaders on the GPU
    shader = glCreateProgram()
    vertex_shader = OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER)
    fragment_shader = OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER)

    # Shader initiation in OpenGL
    glAttachShader(shader, vertex_shader)
    glAttachShader(shader, fragment_shader)
    glLinkProgram(shader)
    glValidateProgram(shader)
    glUseProgram(shader)

    # Garbage collection for the shaders on processor memory
    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)

    return shader


# Uses OpenGL commands to create and setup the GPU buffers
def setup_buffer(render_data, vertices, surfaces):    

    # Formatting vertex data into singe numpy array for OpenGL compatibility
    vertices = numpy.array(vertices, dtype=numpy.float32)

    # Creation and upload of data into the buffers stored on the GPU
    vertex_buffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer)
    glBufferData(GL_ARRAY_BUFFER, render_data["data_size"] * len(vertices), vertices, GL_STATIC_DRAW)

    # Setting of data locations within the buffer so OpenGL can access the data
    position = glGetAttribLocation(render_data["shader"], "position")
    glVertexAttribPointer(position, 2, GL_FLOAT, GL_FALSE, render_data["data_size"] * render_data["line_length"],
                          ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    # Formatting surface data into single numpy array for OpenGL compatibility
    surfaces = numpy.array(surfaces, dtype=numpy.uint32)

    # Clears and uploads the surface data into the surface buffer
    surface_buffer = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, surface_buffer)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, render_data["data_size"] * len(surfaces), surfaces, GL_STATIC_DRAW)

    render_data["surface_buffer"] = surface_buffer

    return render_data


def main():
    pass


if __name__ == "__main__":
    main()

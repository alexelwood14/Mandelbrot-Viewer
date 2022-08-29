# Alex Elwood | June 2020

import glfw
import math
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy


def initiate(resolution, fullscreen, double):
    # Generates all rendering presets and performs OpenGL rendering setup functions

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


def create_shader(double):
    # Defines the shaders and passes them OpenGL on the GPU

    # Defines the vertex shader including its uniforms and functions
    vertex_shader = """
    #version 330
    in vec2 position;
    void main()
    {
        gl_Position =  vec4(position, 0.0f, 1.0f);
    }
    """

    # Defines the fragment shader including its uniforms and functions
    if double:
        fragment_shader = """
        #version 400
        #extension GL_NV_gpu_shader_fp64 : enable
        uniform vec2 resolution;
        uniform float time;
        uniform float scale_factor;
        uniform vec2 translation;
        uniform float max_n;
        out vec4 outColor;
        void main()
        {
            f64vec2 c = f64vec2(double(gl_FragCoord.x / resolution.x), double(gl_FragCoord.y / resolution.y));
            c = (c - 0.5) / scale_factor;
            c.x *= resolution.x / resolution.y;
            c += translation;
            
            f64vec2 z = f64vec2(double(0.0), double(0.0));
            double temp;

            int n;
            for(n=0; n<max_n; n++)
            {
                temp = z.x*z.x - z.y*z.y + c.x;
                z.y = 2.0*z.x*z.y + c.y;
                z.x = temp;
                if(z.x*z.x + z.y*z.y > 4.0) break;
            }


            vec3 colour;
            if (n == max_n)
            {
                colour = vec3(0.0f, 0.0f, 0.0f);
            }
            else
            {
                colour = vec3(n / max_n, 0.4 + (n / max_n * 0.6), 1.0);
            }
            
            outColor = vec4(colour, 1.0f);
        }
        """
    else:
        fragment_shader = """
        #version 400
        uniform vec2 resolution;
        uniform float time;
        uniform float scale_factor;
        uniform vec2 translation;
        uniform float max_n;
        out vec4 outColor;
        void main()
        {
            vec2 c = vec2(gl_FragCoord.x / resolution.x, gl_FragCoord.y / resolution.y);
            c = (c - 0.5) / scale_factor;
            c.x *= resolution.x / resolution.y;
            c += translation;
            
            vec2 z = vec2(0.0f, 0.0f);
            float temp;

            int n;
            for(n=0; n<max_n; n++)
            {
                temp = z.x*z.x - z.y*z.y + c.x;
                z.y = 2.0*z.x*z.y + c.y;
                z.x = temp;
                if(z.x*z.x + z.y*z.y > 4.0) break;
            }


            vec3 colour;
            if (n == max_n)
            {
                colour = vec3(0.0f, 0.0f, 0.0f);
            }
            else
            {
                colour = vec3(n / max_n, 0.4 + (n / max_n * 0.6), 1.0);
            }
            
            outColor = vec4(colour, 1.0f);
        }
        """

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


def setup_buffer(render_data, vertices, surfaces):
    # Uses OpenGL commands to create and setup the GPU buffers

    # Formatting vertex data into singe numpy array for OpenGL compatability
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

    # Formatting surface data into single numpy array for OpenGL compatability
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

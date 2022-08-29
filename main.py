# Alex Elwood | June 2020

import rendering
import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders


def mandelbrot(render_data, resolution, surfaces, double):
    # Record Start Time
    start_time = glfw.get_time()

    # Initiate Uniforms
    res_uni = glGetUniformLocation(render_data["shader"], "resolution")
    glUniform2f(res_uni, resolution[0], resolution[1])
    time_uni = glGetUniformLocation(render_data["shader"], "time")
    scale_uni = glGetUniformLocation(render_data["shader"], "scale_factor")
    trans_uni = glGetUniformLocation(render_data["shader"], "translation")
    max_n_uni = glGetUniformLocation(render_data["shader"], "max_n")

    scale_speed = 1.05
    scale_factor = 0.5

    trans = [-0.66666666, 0]
    max_n = 200

    while True:
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        if glfw.get_key(render_data["window"], 88) == 1:
            print(scale_factor)

        # Inputs for scale factor
        if glfw.get_key(render_data["window"], 87) == 1:  # W
            if double or (not double and scale_factor <= 30000):
                scale_factor *= scale_speed

        elif glfw.get_key(render_data["window"], 83) == 1 and scale_factor >= 0.5:  # S
            scale_factor /= scale_speed

        # Inputs for translation
        move = 0.01
        if glfw.get_key(render_data["window"], 265) and trans[1] < 1.2:  # Up
            trans[1] += move / scale_factor
        elif glfw.get_key(render_data["window"], 264) and trans[1] > -1.2:  # Down
            trans[1] -= move / scale_factor
        if glfw.get_key(render_data["window"], 263) and trans[0] > -2:  # Left
            trans[0] -= move / scale_factor
        elif glfw.get_key(render_data["window"], 262) and trans[0] < 1:  # Right
            trans[0] += move / scale_factor

        # Inputs for max_n
        change = 1
        if glfw.get_key(render_data["window"], 82) and max_n < 500:  # R
            max_n += change
        elif glfw.get_key(render_data["window"], 70) and max_n > 2:  # F
            max_n -= change

        # Inputs for quit
        if glfw.get_key(render_data["window"], 256):
            glfw.terminate()
            exit()

        # Set max_n in shader
        glUniform1f(max_n_uni, max_n)

        # Set translation in shader
        glUniform2f(trans_uni, trans[0], trans[1])

        # Set time in shader
        delta_time = glfw.get_time() - start_time
        glUniform1f(time_uni, delta_time)

        # Set scale factor in shader
        glUniform1f(scale_uni, scale_factor)

        # Renders the camera and map
        glDrawElements(GL_TRIANGLES, len(surfaces), GL_UNSIGNED_INT, None)

        # Pushes rendered frame to the screen
        glfw.swap_buffers(render_data["window"])


def main():
    # Performs all functions needed for initialisation when program is executed

    # Without double precision max zoom is x30,000.
    # With double precision max zoom is x23,230,999,980,401. If it were rendered in its entirety as an image it would
    # contain 72,000,000,000,000,000,000,000,000,000,000,000 (seventy-two decillion) pixels, roughly 8192k.
    double = False

    resolution = [2650, 1440]
    fullscreen = True

    vertices = [-1.0, -1.0,
                1.0, -1.0,
                1.0, 1.0,
                -1.0, 1.0]

    surfaces = [3, 0, 1,
                3, 2, 1]

    # Initiates graphics based functions
    render_data = rendering.initiate(resolution, fullscreen, double)
    render_data = rendering.setup_buffer(render_data, vertices, surfaces)

    # Calls the function to draw the Mandelbrot Set
    mandelbrot(render_data, resolution, surfaces, double)

    glfw.terminate()
    exit()


if __name__ == "__main__":
    main()

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
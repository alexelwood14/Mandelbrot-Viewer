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
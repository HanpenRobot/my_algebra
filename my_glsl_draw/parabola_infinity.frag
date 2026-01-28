#version 300 es
precision highp float;
precision highp int;
out vec4 fragColor;
uniform float u_time;
uniform vec2 u_resolution;
uniform vec2 u_mouse;
const float PI=3.14159265359;
// begin rot
vec2 rot2(vec2 p,float t)
{
    return vec2(cos(t)*p.x-sin(t)*p.y,sin(t)*p.x+cos(t)*p.y);
}
vec3 rotX(vec3 p,float t)
{
    return vec3(p.x,rot2(p.yz,t));
}
vec3 rotY(vec3 p,float t)
{
    return vec3(p.y,rot2(p.zx,t)).zxy;
}
vec3 rotZ(vec3 p,float t)
{
    return vec3(rot2(p.xy,t),p.z);
}
bool grid(vec2 st)
{
    float A=12.;
    return mod(floor(A*st.s)+floor(A*st.t),2.)<1.;
}

// end rot
vec3 text(vec2 st)
{
    
    float delta=.2;
    float B=-1.;
    float B2=B-delta;
    vec3 grid_color=vec3(.1,.4,0.);
    vec3 grid_color2=vec3(1.,1.,1.);
    vec3 curve_color=vec3(0.,0.,1.);
    if((st.t*st.t)<st.s-B)
    {
        if(grid(st))
        {
            return grid_color;
        }
        else
        {
            return grid_color2;
        }
    }
    if((st.t*st.t)<st.s-B2)
    {
        if(grid(st))
        {
            return grid_color;
        }
        else
        {
            return curve_color;
        }
    }
    return grid_color2;
}
void main()
{
    vec2 p=(gl_FragCoord.xy*2.-u_resolution)/min(u_resolution.x,u_resolution.y);
    vec3 cPos=vec3(0.,0.,0.);
    float t=-.5*PI*(u_mouse.y/u_resolution.y);
    vec3 cDir=rotX(vec3(0.,0.,1.),-1.*t);
    vec3 cUp=rotX(vec3(0.,1.,0.),-1.*t);
    vec3 cSide=cross(cDir,cUp);
    float targetDepth=1.;
    vec3 ray=cSide*p.x+cUp*p.y+cDir*targetDepth-cPos;
    ray=normalize(ray);
    vec3 groundNormal=vec3(0.,1.,0.);
    float groundHeight=2.+(u_mouse.x/u_resolution.x);
    if(dot(ray,groundNormal)<0.)
    {
        vec3 hit=cPos-ray*groundHeight/dot(ray,groundNormal);
        fragColor.rgb=text(hit.zx);
    }
    else
    {
        fragColor.rgb=vec3(0.,0.,1.);
    }
    fragColor.a=1.;
}
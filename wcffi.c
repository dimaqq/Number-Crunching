float nextN(float r, float x, int steps)
{
    while (steps > 0)
    {
        steps--;
        x = r * x * (1 - x);
    }
    return x;
}

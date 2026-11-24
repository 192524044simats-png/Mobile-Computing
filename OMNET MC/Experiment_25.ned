simple Experiment25Node
{
    parameters:
        @display("i=block/routing");
    gates:
        input in;
        output out;
}

network Experiment25Network
{
    @display("b=500,300");
    submodules:
        node: Experiment25Node;
}

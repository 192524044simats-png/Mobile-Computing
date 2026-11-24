simple Experiment24Node
{
    parameters:
        @display("i=block/routing");
    gates:
        input in;
        output out;
}

network Experiment24Network
{
    @display("b=500,300");
    submodules:
        node: Experiment24Node;
}

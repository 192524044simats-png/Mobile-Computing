simple Experiment22Node
{
    parameters:
        @display("i=block/routing");
    gates:
        input in;
        output out;
}

network Experiment22Network
{
    @display("b=500,300");
    submodules:
        node: Experiment22Node;
}

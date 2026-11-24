simple Experiment27Node
{
    parameters:
        @display("i=block/routing");
    gates:
        input in;
        output out;
}

network Experiment27Network
{
    @display("b=500,300");
    submodules:
        node: Experiment27Node;
}

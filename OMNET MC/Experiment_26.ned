simple Experiment26Node
{
    parameters:
        @display("i=block/routing");
    gates:
        input in;
        output out;
}

network Experiment26Network
{
    @display("b=500,300");
    submodules:
        node: Experiment26Node;
}

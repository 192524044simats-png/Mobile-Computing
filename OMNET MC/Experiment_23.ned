simple Experiment23Node
{
    parameters:
        @display("i=block/routing");
    gates:
        input in;
        output out;
}

network Experiment23Network
{
    @display("b=500,300");
    submodules:
        node: Experiment23Node;
}

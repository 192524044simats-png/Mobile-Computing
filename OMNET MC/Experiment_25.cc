#include <omnetpp.h>
using namespace omnetpp;

// Experiment 25: Ad Hoc Routing: Proactive (DSDV) versus Reactive (AODV)
class Experiment25Node : public cSimpleModule {
  private:
    int step = 0;
    cOutVector metric;
    cMessage *timer = nullptr;
  protected:
    void initialize() override {
      metric.setName("experimentMetric");
      timer = new cMessage("sampleTimer");
      scheduleAt(simTime(), timer);
    }
    void handleMessage(cMessage *msg) override {
      double value = 0;
      switch (25) {
        case 22: value = 1 + (step >= 3) + (step >= 6); break; // serving cell ID
        case 23: value = 128 + (step % 4) * 32; break;       // frame size
        case 24: value = step + 1; break;                    // signalling count
        case 25: value = 20 + step * 5; break;               // routing delay
        case 26: value = 10 + step * 4; break;                // packets per interval
        case 27: value = 15 + step * 7; break;                // throughput
      }
      metric.record(value);
      EV << "Experiment 25, step=" << step << ", metric=" << value << endl;
      if (++step < 10) scheduleAt(simTime() + 1, timer);
      else cancelAndDelete(timer);
    }
};
Define_Module(Experiment25Node);

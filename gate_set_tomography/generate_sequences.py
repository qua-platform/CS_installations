# %%
import pygsti
from pygsti.modelpacks import smq1Q_XYI

# 1) get the ideal "target" Model (a "stock" model in this case)
mdl_ideal = smq1Q_XYI.target_model()

# 2) generate a GST experiment design
edesign = smq1Q_XYI.create_gst_experiment_design(4) # user-defined: how long do you want the longest circuits?

# 3) write a data-set template
pygsti.io.write_empty_dataset("MyData.txt", edesign.all_circuits_needing_data, "## Columns = 0 count, 1 count")

# STOP! "MyData.txt" now has columns of zeros where actual data should go.
# REPLACE THE ZEROS WITH ACTUAL DATA, then proceed with:
ds = pygsti.io.load_dataset("MyData.txt") # load data -> DataSet object

# OR: Create a simulated dataset with:
# ds = pygsti.data.simulate_data(mdl_ideal, edesign, num_samples=1000)

# 4) run GST (now using the modern object-based interface)
data = pygsti.protocols.ProtocolData(edesign, ds) # Step 1: Bundle up the dataset and circuits into a ProtocolData object
protocol = pygsti.protocols.StandardGST() # Step 2: Select a Protocol to run
results = protocol.run(data) # Step 3: Run the protocol!

# 5) Create a nice HTML report detailing the results
report = pygsti.report.construct_standard_report(results, title="My Report", verbosity=1)
report.write_html("myReport", auto_open=True, verbosity=1) # Can also write out Jupyter notebooks!
# %%

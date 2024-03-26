# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Note: Suppressing FutureWarnings to maintain a clean output. This is specifically to ignore warnings about
# deprecated features in the libraries we're using (e.g., 'use_inf_as_na' option in Pandas, used by Seaborn),
# which we currently have no direct control over. This action is taken to ensure that our output remains
# focused on relevant information, acknowledging that we rely on external library updates to fully resolve
# these deprecations. Always consider reviewing and removing this suppression after significant library updates.
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Constants representing the parameters of the model
ATTACK_RATE = 0.10
TRACE_SUCCESS = 0.20
SECONDARY_TRACE_THRESHOLD = 2


def simulate_event(m):
  """
  Simulates the infection and tracing process for a series of events.
  
  This function creates a DataFrame representing individuals attending weddings and brunches,
  infects a subset of them based on the ATTACK_RATE, performs primary and secondary contact tracing,
  and calculates the proportions of infections and traced cases that are attributed to weddings.
  
  Parameters:
  - m: Dummy parameter for iteration purposes.
  
  Returns:
  - A tuple containing the proportion of infections and the proportion of traced cases
    that are attributed to weddings.
  """
    
    # Create the data for the DataFrame
    event = (['weddng' + str(i) for i in range(1, 3)] * 100) + (['brunch' + str(i) for i in range(1, 81)] * 10)
    infected = [False] * len(event)
    traced = [None] * len(event)

    # Create the DataFrame
    ppl = pd.DataFrame({'event': event, 'infected': infected, 'traced': traced})

    #print(ppl.head())  # Print the first few rows of the DataFrame

    # Explicitly set 'traced' column to nullable boolean type
    ppl['traced'] = ppl['traced'].astype(pd.BooleanDtype())

    # # Infect a random subset of people
    num_infected = int(len(ppl) * ATTACK_RATE)
    infected_indices = np.random.choice(len(ppl), num_infected, replace=False)
    ppl.loc[infected_indices, 'infected'] = True

    # Primary contact tracing: randomly decide which infected people get traced
    infected_indices = np.where(ppl['infected'])[0]
    traced = np.random.rand(sum(ppl['infected'])) <TRACE_SUCCESS
    ppl.loc[infected_indices, 'traced'] = traced

    # Print summary of 'traced' column
    #ppl['traced'].value_counts()

    # Secondary contact tracing based on event attendance

    events_traced = ['weddng1', 'weddng2']  # Example list of events traced

    # Count the occurrences of each event in 'traced' individuals
    event_trace_counts = ppl.loc[ppl['traced'], 'event'].value_counts()

    # Filter events based on SECONDARY_TRACE_THRESHOLD
    events_traced = [event for event, count in event_trace_counts.items() if count >= SECONDARY_TRACE_THRESHOLD]

    # Mark individuals as traced if infected and event is in events_traced
    ppl.loc[ppl['infected'] & ppl['event'].isin(events_traced), 'traced'] = True

    # Print summary of 'traced' column
    #ppl['traced'].value_counts()

    # Calculate event_type
    ppl['event_type'] = ppl['event'].str[0]

    # Calculate proportions of infections and traces attributed to each event type
    wedding_infections = ((ppl['infected']) & (ppl['event_type'] == 'w')).sum()
    brunch_infections = ((ppl['infected']) & (ppl['event_type'] == 'b')).sum()
    p_wedding_infections = wedding_infections / (brunch_infections + wedding_infections)

    wedding_traces = ((ppl['infected']) & (ppl['traced']) & (ppl['event_type'] == 'w')).sum()
    brunch_traces = ((ppl['infected']) & (ppl['traced']) & (ppl['event_type'] == 'b')).sum()
    p_wedding_traces = wedding_traces / (brunch_traces + wedding_traces)

    return p_wedding_infections, p_wedding_traces


# Run the simulation 5000 times
results = [simulate_event(m) for m in range(5000)]
props_df = pd.DataFrame(results, columns=["Infections", "Traces"])

# Plotting the results
plt.figure(figsize=(10, 6))
sns.histplot(props_df['Infections'], color="blue", alpha=0.75, binwidth=0.05, kde=False, label='Infections from Weddings')
sns.histplot(props_df['Traces'], color="red", alpha=0.75, binwidth=0.05, kde=False, label='Traced to Weddings')
plt.xlabel("Proportion of cases")
plt.ylabel("Frequency")
plt.title("Impact of Contact Tracing on Perceived Infection Sources")
plt.legend()
plt.tight_layout()
plt.show()

import defi.defi_tools as dft
import pandas as pd
import streamlit as st




st.title("Defi Strategy Calculator: Hodling vs Stake vs Farm")
st.markdown("![Alt Text](https://media.giphy.com/media/3ov9jNziFTMfzSumAw/giphy.gif?cid=790b7611b961c6b474de2d63bc7b7a34865aa135f4df9f7d&rid=giphy.gif&ct=g)")

st.write("""
Calculate Returns on cryptoassets for staking, farming or simply hodling. The default positions show a scenario as follows:\n

Scenario:\n 
Get returns after 20 days, assuming token A is a stablecoin, token B performs + 150%\n

individual staking pools for both = 0.01% & 0.05% daily\n

liquidity-pool farming rewards =0.2% daily & Earn by fees/day = 0.01%

""")

st.write('---')

st.write('# Please input values as required')

st.write('''## Specify number of days''')
number_days = st.number_input(" Days: ", min_value=1, max_value=999999999, value=20)

st.write('''## First asset price % change''')
asset1_change = st.number_input("asset1 price %Change: ", step=0.1, min_value= -999999999.0, max_value=999999999.0, format="%.4f", value=0.0)

st.write('''## Second asset price % change''')
asset2_change = st.number_input("asset2 price %Change: ", min_value= -999999999.0, max_value=999999999.0,step=0.1,format="%.4f", value=150.0)

st.write('''## Individual daily staking pool reward (%) asset1 ''')
asset1_stake = st.number_input(" % interest: ", min_value= 0.0001, max_value=999999999.0,step=0.1, format="%.4f", value=0.01)

st.write('''## Individual daily staking pool reward (%) asset2 ''')
asset2_stake = st.number_input(" % interest: ", min_value= 0.0001, max_value=999999999.0,step=0.1, format="%.4f", value=0.05)

st.write('''## Liquidity-pool farming daily rewards (%) ''')
asset1_asset2_farm_rewards = st.number_input(" Liquidity farming % interest: ", min_value= 0.0000, max_value=999999999.0,step=0.1, format="%.4f", value=0.2)

st.write('''## Liquidity-pool farming fees/day (%) ''')
asset1_asset2_farm_fees = st.number_input(" Liquidity farming fees/day (%): ", min_value= 0.0001, max_value=999999999.0,step=0.1, format="%.4f", value=0.01)



d = dft.compare(days=number_days, var_A=asset1_change, var_B=asset2_change, rw_pool_A=asset1_stake, rw_pool_B=asset2_stake, rw_pool_AB=asset1_asset2_farm_rewards, fees_AB=asset1_asset2_farm_fees)

df = pd.DataFrame(d.items(), columns=['Strategy', 'Returns'])
df

st.write("## Best Strategy:",(df['Returns'][3]))

# st.write('''## Best Strategy: print(df['Returns'][3])''', print(df['Returns'][3]))

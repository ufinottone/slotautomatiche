
import streamlit as st
import random
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Slot Simulator - Book of Dead", layout="centered")

st.title("🎰 Book of Dead - Slot Simulator")
st.markdown("Simulazione automatica con puntata fissa di **5€**. Budget iniziale: **200€**. Stop win: **+1000€**. Stop loss: **0€**.")

if st.button("🎯 Inizia la simulazione"):
    # Parametri
    starting_balance = 200
    stake = 5
    stop_win = starting_balance + 1000
    stop_loss = 0
    rtp = 0.96
    volatility_factor = 3

    balance = starting_balance
    spins = 0
    log = []

    while stop_loss < balance < stop_win:
        spins += 1
        balance -= stake

        win_probability = rtp / volatility_factor
        if random.random() < win_probability:
            payout_multiplier = random.choices([2, 5, 10, 20, 50, 100], weights=[30, 25, 20, 15, 7, 3])[0]
            win = stake * payout_multiplier
        else:
            win = 0

        balance += win
        log.append((spins, balance, win))

    df = pd.DataFrame(log, columns=["Spin", "Saldo (€)", "Vincita (€)"])
    st.line_chart(df.set_index("Spin")["Saldo (€)"])

    st.success(f"✅ Simulazione terminata dopo {spins} spin.")
    st.write(df)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Scarica il log in CSV", data=csv, file_name="simulazione_book_of_dead.csv", mime="text/csv")

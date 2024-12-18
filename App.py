import streamlit as st
import matplotlib.pyplot as plt

def main():
    st.set_page_config(page_title="Fundraiser Event", layout="wide")

    # Session state to track total funds
    if "total_funds" not in st.session_state:
        st.session_state.total_funds = 0

    # Title and Header
    #st.title("Welcome to Our Fundraiser Event!")
    st.markdown(
        "<h1 style='text-align: center;'>Welcome to Our Fundraiser Event!</h1>",
        unsafe_allow_html=True
    )
    st.header("Make a Difference Today")

    # Layout for Donation and Pie Chart
    col1, col2 = st.columns([1, 1])

    with col2:
        # Introduction Section
        st.subheader("About the Event")
        st.write(
            "Our fundraiser aims to support [cause/charity name]. Every contribution counts towards making a significant impact.")

        # Donation Section
        st.subheader("Donate Now")
        donation_amount = st.number_input("Enter the amount you'd like to donate (in USD):", min_value=1, step=1)
        donor_name = st.text_input("Your Name (optional):")
        submit_donation = st.button("Donate")

        if submit_donation:
            if donation_amount > 0:
                st.session_state.total_funds += donation_amount
                st.success(
                    f"Thank you {donor_name} for your generous donation of ${donation_amount}!{f'' if donor_name else ''}")
            else:
                st.error("Please enter a valid donation amount.")

        # Event Details Section
        st.subheader("Event Details")
        st.write("**Date:** [Insert Date]")
        st.write("**Time:** [Insert Time]")
        st.write("**Location:** [Insert Location]")

    with col1:
        # Fundraising Progress Section
        st.header("Fundraising Progress")

        goal = 10000  # Example fundraising goal
        total_funds = st.session_state.total_funds
        remaining_funds = max(goal - total_funds, 0)
        st.write(f'{total_funds} raised out of {goal}')
        # Pie Chart for Progress
        labels = ["Collected", "Remaining"]
        values = [total_funds, remaining_funds]
        colors = ["#4CAF50", "#FFC107"]

        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90, colors=colors)
        ax.axis("equal")  # Equal aspect ratio ensures the pie chart is a circle.
        st.pyplot(fig)



    # Contact Section
    st.subheader("Contact Us")
    st.write("For inquiries, reach out to us at [email@example.com] or call [phone number].")

if __name__ == "__main__":
    main()

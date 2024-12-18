import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import re
def main():
    st.set_page_config(page_title="Fundraiser Event", layout="wide")

    # Session state to track total funds and donor details
    if "total_funds" not in st.session_state:
        st.session_state.total_funds = 0
    if "donor_data" not in st.session_state:
        st.session_state.donor_data = pd.DataFrame(
            columns=["Name", "Phone Number", "Donation Amount", "Payment Type"]
        )

    # Title and Header
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
            "Our fundraiser aims to support [cause/charity name]. Every contribution counts towards making a significant impact."
        )

        # Donation Section
        st.subheader("Donate Now")
        donor_name = st.text_input("Your Name:")
        phone_number = st.text_input("Your Phone Number:")
        donation_amount = st.number_input("Enter the amount you'd like to donate (in USD):", min_value=1, step=1)

        # Dropdown for Payment Type
        payment_type = st.selectbox(
            "Select Payment Type:", options=["Zelle", "Check", "Cash"]
        )

        submit_donation = st.button("Donate")

        def is_valid_phone_number(number):
            return re.fullmatch(r"\d{10}", number) is not None

        if submit_donation:
            if is_valid_phone_number(phone_number) and donation_amount > 0 and payment_type:
                # Add donation details to session state
                if donor_name == '':
                    donor_name = 'Anonymous'
                new_entry = pd.DataFrame(
                    {
                        "Name": [donor_name],
                        "Phone Number": [phone_number],
                        "Donation Amount": [donation_amount],
                        "Payment Type": [payment_type],
                    }
                )
                st.session_state.donor_data = pd.concat(
                    [st.session_state.donor_data, new_entry], ignore_index=True
                )
                st.session_state.total_funds += donation_amount
                st.success(
                    f"Thank you {donor_name} for your generous donation of ${donation_amount} via {payment_type}!"
                )
            else:
                st.error("Please fill in all the fields before donating.")

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
        st.write(f"{total_funds} raised out of {goal}")
        # Pie Chart for Progress
        labels = ["Collected", "Remaining"]
        values = [total_funds, remaining_funds]
        colors = ["#4CAF50", "#FFC107"]

        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90, colors=colors)
        ax.axis("equal")  # Equal aspect ratio ensures the pie chart is a circle.
        st.pyplot(fig)

    # Download Section
    ADMIN_PASSWORD = "00000"  # Replace with your desired password

    # Display the password input
    st.subheader("Download Donor Details")
    password = st.text_input("Enter Admin Password", type="password")

    if st.button("Submit"):
        if password == ADMIN_PASSWORD:
            st.success("Access Granted! You can now download the donor details.")
            if not st.session_state.donor_data.empty:
                donor_data_csv = st.session_state.donor_data.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="Download Donor Details as CSV",
                    data=donor_data_csv,
                    file_name="donor_details.csv",
                    mime="text/csv",
                )
        else:
            st.error("Access Denied! Incorrect password.")

    # Contact Section
    st.subheader("Contact Us")
    st.write("For inquiries, reach out to us at [email@example.com] or call [phone number].")

if __name__ == "__main__":
    main()

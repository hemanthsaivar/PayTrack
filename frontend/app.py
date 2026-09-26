import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import httpx
import streamlit as st
from frontend.client import call
from frontend.state import initialize_state

st.set_page_config(page_title='PayTrack', page_icon='🧾', layout='wide')
initialize_state(st.session_state)
st.title('PayTrack · Debugging Lab')
st.caption('Mock payments only · amounts are entered as integer paise · ₹1 = 100 paise')
page = st.sidebar.radio('Workspace', ['Invoices', 'New invoice', 'Payments', 'Reports'])

try:
    if page == 'Invoices':
        paid = st.checkbox('Show paid invoices only', key='show_paid_only')
        offset = st.number_input('Offset', min_value=0, step=1)
        if st.button('Refresh'):
            st.rerun()
        params = {'limit':20, 'offset':offset}
        if paid:
            params['status'] = 'paid'
        st.dataframe(call('GET', '/invoices', params=params), use_container_width=True)
        with st.form('note'):
            invoice_id = st.number_input('Invoice ID', min_value=1, step=1)
            note = st.text_area('Note')
            if st.form_submit_button('Save note'):
                call('PATCH', f'/invoices/{invoice_id}/note', json={'note':note})
                st.success('Note saved. Refresh to verify.')
    elif page == 'New invoice':
        with st.form('invoice'):
            customer = st.text_input('Customer', value='Demo customer')
            description = st.text_input('Description', value='Consulting')
            price = st.number_input('Unit price (paise)', min_value=1, value=10000, step=1)
            quantity = st.number_input('Quantity', min_value=0, value=1, step=1)
            if st.form_submit_button('Create invoice'):
                result = call('POST', '/invoices', json={'customer':customer, 'items':[
                    {'description':description, 'unit_price_paise':price, 'quantity':quantity}]})
                st.success(f"Created invoice {result['id']}: ₹{result['amount_paise']/100:.2f}")
    elif page == 'Payments':
        st.info('Payment ledger is independent of invoice status in this lab. It does not automatically settle invoices.')
        with st.form('payment'):
            invoice_id = st.number_input('Invoice ID', min_value=1, step=1)
            amount = st.number_input('Payment amount (paise)', min_value=1, value=1000, step=1)
            request_key = st.text_input('Request key (reuse when retrying)', value='demo-payment-1')
            failed = st.checkbox('Simulate failure')
            if st.form_submit_button('Record payment'):
                st.json(call('POST', '/payments', json={'invoice_id':invoice_id,
                    'amount_paise':amount,'request_key':request_key,'simulate_failure':failed}))
        with st.form('refund'):
            payment_id = st.number_input('Payment ID', min_value=1, step=1)
            refund = st.number_input('Refund amount (paise)', min_value=1, step=1)
            if st.form_submit_button('Refund'):
                st.json(call('POST', f'/payments/{payment_id}/refund', json={'amount_paise':refund}))
    else:
        report = call('GET', '/reports/summary')
        st.metric('Net collected', f"₹{report['net_paise']/100:.2f}")
        st.download_button('Download invoice CSV', call('GET','/reports/invoices.csv'),
                           file_name='invoices.csv', mime='text/csv')
except httpx.HTTPStatusError as exc:
    st.error(f'API returned {exc.response.status_code}: {exc.response.text}')
except httpx.RequestError:
    st.error('Cannot reach API. Start FastAPI on port 8000, then refresh.')

import re

def parse_option_symbol(symbol):
    """
    Expected format:
    NIFTY260224C25500
    """

    if not symbol:
        return "N/A", "N/A", "N/A", "N/A"

    # Regex breakdown:
    # Group1 = underlying
    # Group2 = expiry
    # Group3 = C or P
    # Group4 = strike
    match = re.match(r"([A-Z]+)(\d{6})([CP])(\d+)", symbol)

    if not match:
        return symbol, "N/A", "N/A", "N/A"

    underlying = match.group(1)
    expiry_raw = match.group(2)
    option_type = match.group(3)
    strike = match.group(4)

    # Convert expiry 260224 → 26-02-24
    expiry = f"{expiry_raw[:2]}-{expiry_raw[2:4]}-{expiry_raw[4:]}"

    option_type_full = "CE" if option_type == "C" else "PE"

    return underlying, expiry, strike, option_type_full


def format_signal_message(data):

    signal_type = data.get("type", "N/A")
    current_symbol = data.get("current_symbol", "")

    pivot = data.get("pivot_price", "N/A")
    confirm = data.get("confirm_price", "N/A")

    ce_status = data.get("ce_status", "")
    pe_status = data.get("pe_status", "")

    time_ist = data.get("confirm_time", "N/A")

    current_chart = data.get("current_chart", "")
    opposite_chart = data.get("opposite_chart", "")

    manual_link = "https://www.tradingview.com/chart/NJntjUQW/"

    # Parse symbol
    underlying, expiry, strike, option_type = parse_option_symbol(current_symbol)

    message = (
        f"<b>🚀 BREAKOUT SIGNAL</b>\n\n"
        f"<b>Signal:</b> {signal_type}\n\n"

        f"<b>Underlying:</b> {underlying}\n"
        f"<b>Expiry:</b> {expiry}\n"
        f"<b>Strike:</b> {strike} {option_type}\n\n"

        f"<b>CE Status:</b> {ce_status}\n"
        f"<b>PE Status:</b> {pe_status}\n\n"

        f"<b>Pivot:</b> {pivot}\n"
        f"<b>Confirm:</b> {confirm}\n\n"

        f"<b>Time:</b> {time_ist}\n\n"

        f"📊 <a href=\"{current_chart}\">Current Chart</a>\n\n"
        f"📉 <a href=\"{opposite_chart}\">Opposite Chart</a>\n\n"

        f"⚠️ <b>Manual Confirmation:</b>\n"
        f"{manual_link}"
    )

    return message

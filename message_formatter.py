def format_signal_message(data):

    signal_type = data.get("type", "N/A")
    current_symbol = data.get("current_symbol", "N/A")
    opposite_symbol = data.get("opposite_symbol", "N/A")

    pivot = data.get("pivot_price", "N/A")
    confirm = data.get("confirm_price", "N/A")

    ce_status = data.get("ce_status", "")
    pe_status = data.get("pe_status", "")

    time_ist = data.get("confirm_time", "N/A")

    current_chart = data.get("current_chart", "")
    opposite_chart = data.get("opposite_chart", "")

    manual_link = "https://www.tradingview.com/chart/NJntjUQW/"

    message = (
        f"<b>🚀 BREAKOUT SIGNAL</b>\n\n"
        f"<b>Type:</b> {signal_type}\n"
        f"<b>Symbol:</b> {current_symbol}\n\n"
        f"<b>CE Status:</b> {ce_status}\n"
        f"<b>PE Status:</b> {pe_status}\n\n"
        f"<b>Pivot:</b> {pivot}\n"
        f"<b>Confirm:</b> {confirm}\n\n"
        f"<b>Time:</b> {time_ist}\n\n"
        f"📊 <a href=\"{current_chart}\">Current Chart</a>\n"
        f"📉 <a href=\"{opposite_chart}\">Opposite Chart</a>\n\n"
        f"⚠️ <b>Manual Confirmation:</b>\n"
        f"<a href=\"{manual_link}\">Open Strategy Monitor</a>"
    )

    return message

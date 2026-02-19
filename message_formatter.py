def format_signal_message(data):
    return (
        f"<b>🚀 BREAKOUT SIGNAL</b>\n\n"
        f"<b>Type:</b> {data.get('type')}\n"
        f"<b>Symbol:</b> {data.get('ticker')}\n\n"
        f"<b>Pivot:</b> {data.get('pivot_price')}\n"
        f"<b>Confirm:</b> {data.get('confirm_price')}\n\n"
        f"<b>Time:</b> {data.get('confirm_time')}\n\n"
        f"<a href=\"{data.get('chart')}\">📊 Open Chart</a>"
    )

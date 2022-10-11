def handle_respone(message) -> str:
  p_message = message.lower()

  if p_message == '$hey':
    return 'Yo !'

  if p_message == '$help':
    return 'Help'
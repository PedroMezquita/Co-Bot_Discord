import database

def handle_respone(message, author) -> str:
  p_message = message.lower()
  res = p_message.split()
  p_command = str(res[0])

  match p_command:
    case '$hey':
      return 'Yo !'
    
    case '$help':
      return 'Help'

    case '$buy':
      data = database.DataBase()
      response = data.buy(message, author)
      return response

    case '$shop':
      data = database.DataBase()
      response = data.shop()
      return response

    case '$clear_list':
      data = database.DataBase()
      reponse = data.clear_list(res)
      return reponse
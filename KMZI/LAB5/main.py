import CIK, Voter, CSK

print("ЦИК создает и публикует список всех избирателей...")
CIK.generate_voter_list(20)  #ЦИК публикует список всех правомочных избирателей

print("ЦИК создает пару ключей...")
CIK.generate_key_pair() #ЦИК создает пару ключей для асимметричного шифрования 

print("ЦИК публикует открытый ключ в ЦСК...") #это происходит в CSK.py
CSK.get_cik_key()

print("Избиратели публикуют свои ID и ключ в ЦСК...")
Voter.generate_specific_voters_data_list()  #создается список с нужной инфой о изберателях(ID, ключи, метки и тд)
CSK.get_voters_info()

print("Избиратели генерируют свою уникальную метку...") #происходит в voter.py

print("Избиратели ослепляют и подписывают свои метки и отправляют в ЦИК...")
Voter.blinding_protocol()

print("ЦИК проверяет ЭЦП избирателей и отправляет избирателям слепую ЭЦП...")
CIK.check_signature()

print("Избиратели снимают закрывающий множитель с ЭЦП комиссии...")
Voter.remove_r()

print("Избиратели голосуют...")  #это происходит сразу в remove_r

print("Отправка анонимных результатов в ЦИК...") #также в remove_r

print("ЦИК проверяет данные и публикует метку и бюллитень и выводит результат")
CIK.verify_and_results()
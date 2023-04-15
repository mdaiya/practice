while True:

    #身長入力
    try:
        height_cm=input('身長(cm)を教えてください：')
        height_cm=float(height_cm)                          #inputでの入力は文字列となるので、小数に変換
        height_m=height_cm/100                              #単位cm → m
    except:
        print('入力に間違いがあります。もう一度やり直してください。')
        break

    #体重入力
    try:
        weight=input('体重(kg)を教えてください：')
        weight=float(weight)
    except:
        print('入力に間違いがあります。もう一度やり直してください。')
        break    

    #BMI計算
    bmi=weight/pow(height_m,2)

    #BMI結果出力
    print('BMI値は{:.1f}です。'.format(bmi))                 #BMI値を小数第一位まで出力指定
    if bmi<18.5:
        print('少しやせすぎです。')
        break
    elif 18.5<=bmi<25.0:
        print('標準的な体系です。')
        break
    elif 25.0<=bmi<30.0:
        print('少し太っています。')
        break
    else:
        print('高度の肥満です。')
        break
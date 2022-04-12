# >_ <- условное обозначение начала комментакия (нигде больше не применяется, использую просто для удобства)

# >_ подключение библиотеки компьютерного зрения
import cv2

# >_ объявляем индификатор камеры ( подключаем камеру к проекту)
# >_ ВАЖНО! чтобы камера была свободна (все приложения, использующие камеру, должны быть закрыты)
cap = cv2.VideoCapture( 0 )

# запускаем бесконечный цикл
while True:
    # >_ считываем изображение с камеры с помощью вункции read , обращаясь через
    #      индификатор камеры cap 
    # >_ в переменную rt записывается True, если считать удалось, и
    #      False, если по какой-то причине изображение считать не удалось (в проекте не используется)
    # >_ в переменную frame записывается значение нашего кадра в виде массива numpy
    ret, frame = cap.read()

    # >_  переводим кадр frame из формата  BGR в формат HSV
    frame_HSV = cv2.cvtColor( frame, cv2.COLOR_BGR2HSV )



    
    # >_ задаем минимальные и максимальные значения нашего цвете в пространстве HSV

    # >_ в clr_low  записываются ТОЛЬКО минимальные значения
    # >_ в clr_high записываются ТОЛЬКО максимальные значения

    # >_ H - Hue - цветовой тон. Первое значение в кортеже ( первое число в круглых скобках )
    #      Минимальное значение - 0, максимальное - 180 
    #      Позволяет выбрать ЛЮБОЙ цвет. 
    #      (смотреть по шкале hue (надеюсь, не забуду приложить) )

    # >_ S - Saturation - насыщенность. Второе значение в кортеже (второе число в круглых скобках)
    #      Определяет, насколько цвет светлый (белый)
    #      чем меньше значение, тем более светлый цвет ищет

    # >_ V- Value, same Brightness - значение цвета, оно же яркость
    #      Определяет, насколько цвет тусклый (чёрный)
    #      чем меньше значение, тем более тёмный цвет ищет
    
              #(  H,   S,   V )
    clr_low  = (  0, 210, 110 )
    clr_high = ( 15, 255, 255 )
    
    # >_ находим цветовой промежуток (изображение-маску) функцией inRangе
    frame_clr = cv2.inRange( frame_HSV, clr_low, clr_high )

    # >_ показываем кадр frame, взятый с камеры
    cv2.imshow( 'main', frame )
    
    # >_ показываем маску цвета (она черно-белая )
    cv2.imshow( 'frame mask', frame_clr )

    # >_ условие прерывания
    #     По нажатию на кнопку 'q' на клавиатуре завершается работа программы
    if cv2.waitKey( 1 ) == ord( 'q' ):
        break

# >_ завершение работы с камерой
#     Нужно для освобождения камеры для других приложений
cap.release()

# >_ закрытие всех созданных окон
cv2.destroyAllWindows()
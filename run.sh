#!/bin/bash     #это значит, что этот файл надо выполнять через bash 

echo "Starting mail processor..."     #выводим сообщение о том, что запуск начался


if [! -d "inbox"]; then     #если папки "inbox" нет, то
    echo "Error: Inbox directory not found!"     #выводим сообщение об ошибке
    exit 1     #завершаем выполнение c ошибкой
fi


if [! -d "processed"]; then     #если папки "processed" нет, то
    echo "Processed folder not found, creating it..."     #выводим сообщение о том, что папка не найдена и будет создана
    mkdir processed     #и создаем ее 
fi


if [-f "requirements.txt"]; then     #если файл "requirements.txt" существует, то
    echo "Installing required Python libraries..."  #выводим, что устанавливаем необходимые библиотеки
    python3 -m pip install -r requirements.txt  #сама установка 
else
    echo "Warning: requirements.txt not found, skipping library installation."  #выводим предупреждение, что файл не найден и установка пропущена
fi  


echo "Running application..."  # выводим соо, о том, что запускаем приложение
python3 -m app.main     #запускаем основную программу


if [ $? -eq 0 ]; then   # $? - это результат предыдущей команды, если он равен 0, значит все ок, команда выполнена
    echo "Processing completed successfully"
else
    echo "Processing failed"  #выводим сообщение об ошибке 
    exit 1      #завершаем выполнение c ошибкой
fi


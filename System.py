import platform
import psutil
import cpuinfo

def get_system_info():
    try:
        # Имя компьютера
        computer_name = platform.node()

        # Операционная система
        os_info = platform.platform()

        # Процессор
        cpu_info = cpuinfo.get_cpu_info()
        cpu_name = cpu_info['brand_raw']
        cpu_cores = psutil.cpu_count(logical=False)

        # ОЗУ
        ram = psutil.virtual_memory()
        total_ram = ram.total / (1024 ** 3)
        ram_slots = 'информация недоступна в psutil'

        # Видеокарта
        gpu_info = 'информация недоступна в стандартных библиотеках'

        # Диски
        disk_info = psutil.disk_partitions()
        disk_sizes = {d.device: psutil.disk_usage(d.mountpoint).total / (1024 ** 3) for d in disk_info}

        # Температура процессора (доступно не во всех системах)
        temperature = 'информация недоступна'
        
        print(f"Имя компьютера: {computer_name}")
        print(f"Операционная система: {os_info}")
        print(f"Процессор: {cpu_name}")
        print(f"Количество ядер: {cpu_cores}")
        print(f"Общее ОЗУ: {total_ram:.2f} GB")
        print(f"Информация о слотах ОЗУ: {ram_slots}")
        print(f"Информация о видеокарте: {gpu_info}")
        print("Размеры дисков:")
        for disk, size in disk_sizes.items():
            print(f"{disk}: {size:.2f} GB")
        print(f"Температура процессора: {temperature}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    get_system_info()

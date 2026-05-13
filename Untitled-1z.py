def todo_list():
    tasks = []
    
    while True:
        print("\n" + "=" * 30)
        print("   قائمة المهام 📝")
        print("=" * 30)
        print("1. عرض المهام")
        print("2. إضافة مهمة")
        print("3. حذف مهمة")
        print("4. إنهاء")
        
        choice = input("اختيارك: ")
        
        if choice == '1':
            print("\n📋 المهام:")
            if not tasks:
                print("   لا توجد مهام!")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"   {i}. {task}")
        
        elif choice == '2':
            task = input("أدخل المهمة الجديدة: ")
            tasks.append(task)
            print(f"✅ تمت إضافة: {task}")
        
        elif choice == '3':
            if not tasks:
                print("⚠️ لا توجد مهام للحذف!")
            else:
                try:
                    num = int(input("رقم المهمة للحذف: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        print(f"🗑️ تم حذف: {removed}")
                    else:
                        print("⚠️ رقم غير صحيح!")
                except ValueError:
                    print("⚠️ الرجاء إدخال رقم!")
        
        elif choice == '4':
            print("👋 إلى اللقاء!")
            break
        
        else:
            print("⚠️ اختيار غير صحيح!")

# تشغيل البرنامج
todo_list()
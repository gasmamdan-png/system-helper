#!/usr/bin/env python3
"""
System Helper - تطبيق مساعد النظام للأندرويد
واجهة Kivy بسيطة مع دعم اللغة العربية
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
import threading
import json
import uuid
import platform
from datetime import datetime
import os

# تحميل ملف KV
Builder.load_file('systemhelper.kv')

class SystemHelperScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # بدء الخدمة في الخلفية بعد ثانيتين
        Clock.schedule_once(self.start_background_service, 2)
    
    def toggle_service(self, instance, value):
        """تبديل حالة الخدمة"""
        if value:
            self.ids.service_status.text = 'نشطة 🟢'
            self.ids.service_status.color = (0.3, 0.7, 0.4, 1)
            self.start_service()
        else:
            self.ids.service_status.text = 'غير نشطة 🔴'
            self.ids.service_status.color = (0.9, 0.3, 0.3, 1)
            self.stop_service()
    
    def start_service(self):
        """بدء الخدمة في الخلفية"""
        threading.Thread(target=self.run_background_service, daemon=True).start()
    
    def stop_service(self):
        """إيقاف الخدمة"""
        print("🛑 إيقاف خدمة المراقبة")
    
    def run_background_service(self):
        """تشغيل الخدمة في الخلفية"""
        try:
            print("🔒 بدء خدمة المراقبة في الخلفية...")
            
            # حفظ معلومات الجهاز
            device_info = {
                "device_id": str(uuid.uuid4())[:8],
                "device_name": f"Android_{platform.node()}",
                "connected_at": datetime.now().isoformat(),
                "status": "active",
                "developer": "غمدان قاسم",
                "contact": "774966450"
            }
            
            # حفظ في ملف JSON
            with open("device_info.json", "w", encoding="utf-8") as f:
                json.dump(device_info, f, indent=4, ensure_ascii=False)
            
            print(f"✅ معلومات الجهاز: {device_info}")
            
            # تشغيل كود frte4.py في الخلفية
            self.run_spy_service()
            
        except Exception as e:
            print(f"❌ خطأ في الخدمة: {e}")
    
    def run_spy_service(self):
        """تشغيل خدمة المراقبة"""
        try:
            # محاولة تشغيل كود frte4.py
            print("📡 بدء خدمة المراقبة...")
            
            # هنا يمكن استيراد وتشغيل كود frte4.py
            # import frte4
            
        except Exception as e:
            print(f"⚠️ تعذر تشغيل خدمة المراقبة: {e}")
    
    def start_background_service(self, dt):
        """بدء الخدمة تلقائياً عند التشغيل"""
        # يمكن تفعيل هذه الميزة لاحقاً
        pass
    
    def show_settings(self):
        """عرض نافذة الإعدادات"""
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        settings_label = Label(
            text="إعدادات التطبيق:\n\n1. صلاحيات التخزين\n2. صلاحيات الإنترنت\n3. صلاحيات النظام\n4. خدمات الخلفية\n5. الإشعارات",
            font_size='16sp',
            color=(1, 1, 1, 1),
            halign='center'
        )
        settings_label.bind(size=settings_label.setter('text_size'))
        
        close_btn = Button(
            text="إغلاق ✕",
            size_hint=(1, 0.3),
            background_color=(0.9, 0.3, 0.3, 1)
        )
        
        content.add_widget(settings_label)
        content.add_widget(close_btn)
        
        popup = Popup(
            title='الإعدادات ⚙️',
            content=content,
            size_hint=(0.8, 0.6)
        )
        
        close_btn.bind(on_press=popup.dismiss)
        popup.open()
    
    def show_about(self):
        """عرض نافذة حول التطبيق"""
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        scroll = ScrollView()
        
        about_text = (
            "System Helper v1.0\n\n"
            "تطبيق مساعد للنظام\n"
            "يعمل على تحسين أداء الجهاز\n"
            "ويقدم خدمات النظام المختلفة\n\n"
            "المميزات:\n"
            "✅ مراقبة النظام\n"
            "✅ تحسين الأداء\n"
            "✅ خدمات خلفية\n"
            "✅ واجهة عربية\n"
            "✅ دعم متعدد اللغات\n"
            "✅ تحديثات تلقائية\n\n"
            "المطور: غمدان قاسم\n"
            "رقم التواصل: 774966450\n\n"
            "تاريخ الإصدار: 2024\n"
            "© جميع الحقوق محفوظة"
        )
        
        about_label = Label(
            text=about_text,
            font_size='16sp',
            color=(1, 1, 1, 1),
            halign='center',
            valign='middle',
            text_size=(None, None),
            size_hint_y=None,
            height=500
        )
        about_label.bind(texture_size=about_label.setter('size'))
        
        scroll.add_widget(about_label)
        
        close_btn = Button(
            text="إغلاق ✕",
            size_hint=(1, 0.2),
            background_color=(0.2, 0.5, 0.8, 1)
        )
        
        content.add_widget(scroll)
        content.add_widget(close_btn)
        
        popup = Popup(
            title='حول التطبيق ℹ️',
            content=content,
            size_hint=(0.8, 0.7)
        )
        
        close_btn.bind(on_press=popup.dismiss)
        popup.open()

class SystemHelperApp(App):
    def build(self):
        # تعيين خلفية التطبيق
        Window.clearcolor = (0.1, 0.1, 0.15, 1)  # خلفية داكنة
        self.title = "System Helper - مساعد النظام"
        
        # إضافة اسم المطور في عنوان النافذة
        Window.set_title(f"{self.title} | المطور: غمدان قاسم")
        
        # إنشاء الشاشة الرئيسية
        return SystemHelperScreen()

if __name__ == '__main__':
    SystemHelperApp().run()
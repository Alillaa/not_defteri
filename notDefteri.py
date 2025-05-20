import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QAction,
                             QFileDialog, QMessageBox, QFontDialog, QMenu, QStatusBar)
from PyQt5.QtGui import QIcon, QKeySequence, QFont, QFontMetrics, QFontDatabase, QFontInfo
from PyQt5.QtCore import Qt, QSysInfo, QDate


DARK_STYLE = """
QMainWindow {
    background-color: #2E2E2E; color: #F0F0F0;
}
QTextEdit {
    background-color: #3C3C3C; color: #F0F0F0; border: 1px solid #555555;
    selection-background-color: #5A5A5A; selection-color: #FFFFFF;
}
QMenuBar {
    background-color: #383838; color: #F0F0F0; border-bottom: 1px solid #555555;
    font-family: "Consolas", "DejaVu Sans Mono", "Courier New", monospace; font-size: 10pt;
}
QMenuBar::item { background-color: transparent; padding: 4px 10px; color: #F0F0F0; }
QMenuBar::item:selected { background-color: #5A5A5A; color: #FFFFFF; }
QMenuBar::item:pressed { background-color: #6A6A6A; }
QMenu {
    background-color: #3C3C3C; color: #F0F0F0; border: 1px solid #555555; padding: 5px;
    font-family: "Consolas", "DejaVu Sans Mono", "Courier New", monospace; font-size: 10pt;
}
QMenu::item { padding: 5px 20px 5px 20px; }
QMenu::item:selected { background-color: #5A5A5A; color: #FFFFFF; }
QMenu::separator { height: 1px; background-color: #555555; margin-left: 10px; margin-right: 5px; }
QStatusBar { background-color: #383838; color: #F0F0F0; border-top: 1px solid #555555; }
QDialog { background-color: #2E2E2E; color: #F0F0F0;
          font-family: "Consolas", "DejaVu Sans Mono", "Courier New", monospace; font-size: 10pt;}
QDialog QPushButton { background-color: #5A5A5A; color: #FFFFFF; border: 1px solid #777777; padding: 6px 12px; min-width: 70px; }
QDialog QPushButton:hover { background-color: #6A6A6A; }
QDialog QPushButton:pressed { background-color: #4A4A4A; }
QDialog QLabel { color: #F0F0F0; }
QLineEdit { background-color: #3C3C3C; color: #F0F0F0; border: 1px solid #555555; padding: 3px; }
"""

LIGHT_CUSTOM_STYLE = """
QMainWindow { background-color: #F0F0F0; color: #333333; }
QTextEdit {
    background-color: #FFFFFF; color: #222222; border: 1px solid #C0C0C0;
    selection-background-color: #AED6F1; selection-color: #1C1C1C;
}
QMenuBar { background-color: #E8E8E8; color: #333333; border-bottom: 1px solid #D0D0D0;
           font-family: "Segoe UI", "Arial", sans-serif; font-size: 9pt;}
QMenuBar::item { background-color: transparent; padding: 4px 10px; }
QMenuBar::item:selected { background-color: #D5D5D5; }
QMenuBar::item:pressed { background-color: #C5C5C5; }
QMenu { background-color: #FEFEFE; color: #333333; border: 1px solid #CCCCCC; padding: 5px;
        font-family: "Segoe UI", "Arial", sans-serif; font-size: 9pt;}
QMenu::item { padding: 5px 20px 5px 20px; }
QMenu::item:selected { background-color: #AED6F1; color: #1C1C1C; }
QMenu::separator { height: 1px; background-color: #E0E0E0; margin-left: 10px; margin-right: 5px; }
QStatusBar { background-color: #E8E8E8; color: #333333; border-top: 1px solid #D0D0D0; }
QDialog { background-color: #F0F0F0; color: #333333;
          font-family: "Segoe UI", "Arial", sans-serif; font-size: 9pt;}
QDialog QPushButton {
    background-color: #DDEEFF; color: #224466; border: 1px solid #AACCFF;
    padding: 6px 12px; min-width: 70px; border-radius: 3px;
}
QDialog QPushButton:hover { background-color: #CCDDEE; }
QDialog QPushButton:pressed { background-color: #BBDDFF; }
QLineEdit { background-color: #FFFFFF; color: #222222; border: 1px solid #C0C0C0; padding: 3px; }
"""

SEPIA_STYLE = """
QMainWindow {
    background-color: #F3EFEB; color: #4A3B31;
}
QTextEdit {
    background-color: #FCF8F3; color: #5D4037; border: 1px solid #D7C8B9;
    selection-background-color: #BCAAA4; selection-color: #FFFFFF;
}
QMenuBar {
    background-color: #E8E0D9; color: #4A3B31; border-bottom: 1px solid #D7C8B9;
    font-family: "Georgia", serif; font-size: 10pt;
}
QMenuBar::item { background-color: transparent; padding: 4px 10px; color: #4A3B31; }
QMenuBar::item:selected { background-color: #D7C8B9; color: #31271F; }
QMenuBar::item:pressed { background-color: #C8B9A9; }
QMenu {
    background-color: #F3EFEB; color: #4A3B31; border: 1px solid #D7C8B9; padding: 5px;
    font-family: "Georgia", serif; font-size: 10pt;
}
QMenu::item { padding: 5px 20px 5px 20px; }
QMenu::item:selected { background-color: #D7C8B9; color: #31271F; }
QMenu::separator { height: 1px; background-color: #D7C8B9; margin-left: 10px; margin-right: 5px; }
QStatusBar { background-color: #E8E0D9; color: #4A3B31; border-top: 1px solid #D7C8B9; }
QDialog { background-color: #F3EFEB; color: #4A3B31;
          font-family: "Georgia", serif; font-size: 10pt;}
QDialog QPushButton {
    background-color: #BCAAA4; color: #FFFFFF; border: 1px solid #A99A8D;
    padding: 6px 12px; min-width: 70px; border-radius: 3px;
}
QDialog QPushButton:hover { background-color: #A99A8D; }
QDialog QPushButton:pressed { background-color: #998B7D; }
QDialog QLabel { color: #4A3B31; }
QLineEdit { background-color: #FCF8F3; color: #5D4037; border: 1px solid #D7C8B9; padding: 3px; }
"""

FLORAL_STYLE = """
QMainWindow {
    background-image: url("C:/Users/aleyn/OneDrive/Masaüstü/9549_White-and-pink-flowers-with-water-drops.jpg");
    background-repeat: no-repeat; 
    background-position: center center; 
    background-attachment: fixed;
}
QTextEdit {
    background-color: rgba(255, 255, 255, 0.88); 
    color: #1E1E1E;
    border: 1px solid rgba(100, 100, 100, 0.5);
    selection-background-color: #77B5FE;
    selection-color: white;
}
QMenuBar {
    background-color: rgba(230, 230, 230, 0.75); 
    color: #222222;
    border-bottom: 1px solid rgba(180, 180, 180, 0.6);
    font-family: "Segoe UI", "Arial", sans-serif; font-size: 9pt;
}
QMenuBar::item {
    background-color: transparent;
    padding: 4px 10px;
    color: #222222;
}
QMenuBar::item:selected {
    background-color: rgba(173, 216, 230, 0.8);
    color: #111111;
}
QMenu {
    background-color: rgba(245, 245, 245, 0.92); 
    color: #222222;
    border: 1px solid rgba(170, 170, 170, 0.8);
    padding: 5px;
    font-family: "Segoe UI", "Arial", sans-serif; font-size: 9pt;
}
QMenu::item:selected {
    background-color: rgba(173, 216, 230, 0.8);
    color: #111111;
}
QMenu::separator {
    height: 1px;
    background-color: rgba(190, 190, 190, 0.7);
    margin-left: 10px;
    margin-right: 5px;
}
QStatusBar {
    background-color: rgba(230, 230, 230, 0.75);
    color: #222222;
    border-top: 1px solid rgba(180, 180, 180, 0.6);
}
QDialog {
    background-color: rgba(240, 240, 240, 0.97); 
    color: #222222;
    border: 1px solid #999999;
    font-family: "Segoe UI", "Arial", sans-serif; font-size: 9pt;
}
QDialog QPushButton {
    background-color: rgba(210, 225, 240, 0.9);
    color: #111111;
    border: 1px solid #909090;
    padding: 6px 12px;
    min-width: 70px;
    border-radius: 3px;
}
QDialog QPushButton:hover {
    background-color: rgba(190, 210, 230, 0.95);
}
QDialog QPushButton:pressed {
    background-color: rgba(170, 190, 210, 0.95);
}
QLineEdit {
    background-color: rgba(255, 255, 255, 0.9);
    color: #222222;
    border: 1px solid #B0B0B0;
    padding: 3px;
}
"""


class ThemedNotepad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_file = None
        self.base_window_title = "Not Defteri"
        
        self.base_font_family = "Consolas"
        self.base_font_size = 11


        self.current_theme_style = FLORAL_STYLE
        self.current_theme_name = "floral"

        self.initUI()
        
       
        self.statusBar().showMessage(f"{self.base_window_title} Hazır.")
        self.update_window_title() 


    def initUI(self):
        self.text_area = QTextEdit()
        self.text_area.setAcceptRichText(False)
        self.setCentralWidget(self.text_area)
        self.text_area.document().modificationChanged.connect(self.update_window_title)

        self.setStatusBar(QStatusBar(self))

        menubar = self.menuBar()

        file_menu = menubar.addMenu('&Dosya')
        actions_file = [
            ('&Yeni', QKeySequence.New, 'Yeni bir dosya oluştur', self.new_file, "document-new"),
            ('&Aç...', QKeySequence.Open, 'Varolan bir dosyayı aç', self.open_file, "document-open"),
            ('&Kaydet', QKeySequence.Save, 'Dosyayı kaydet', self.save_file, "document-save"),
            ('Farklı &Kaydet...', QKeySequence.SaveAs, 'Dosyayı farklı bir isimle kaydet', self.save_as_file, "document-save-as"),
            None,
            ('&Çıkış', QKeySequence.Quit, 'Uygulamadan çık', self.close, "application-exit")
        ]
        for item_data in actions_file:
            if item_data is None: file_menu.addSeparator(); continue
            text, shortcut, tip, callback, icon_name = item_data
            action = QAction(QIcon.fromTheme(icon_name), text, self)
            if isinstance(shortcut, QKeySequence): action.setShortcut(shortcut)
            action.setStatusTip(tip); action.triggered.connect(callback); file_menu.addAction(action)

        edit_menu = menubar.addMenu('&Düzenle')
        actions_edit = [
            ('&Geri Al', QKeySequence.Undo, 'Son işlemi geri al', self.text_area.undo, "edit-undo"),
            ('&Yinele', QKeySequence.Redo, 'Geri alınan son işlemi yinele', self.text_area.redo, "edit-redo"),
            None,
            ('Ke&s', QKeySequence.Cut, 'Seçili metni kes', self.text_area.cut, "edit-cut"),
            ('&Kopyala', QKeySequence.Copy, 'Seçili metni kopyala', self.text_area.copy, "edit-copy"),
            ('&Yapıştır', QKeySequence.Paste, 'Panodaki metni yapıştır', self.text_area.paste, "edit-paste"),
            None,
            ('Tümünü &Seç', QKeySequence.SelectAll, 'Tüm metni seç', self.text_area.selectAll, "edit-select-all")
        ]
        for item_data in actions_edit:
            if item_data is None: edit_menu.addSeparator(); continue
            text, shortcut, tip, callback, icon_name = item_data
            action = QAction(QIcon.fromTheme(icon_name), text, self)
            if isinstance(shortcut, QKeySequence): action.setShortcut(shortcut)
            action.setStatusTip(tip); action.triggered.connect(callback); edit_menu.addAction(action)

        format_menu = menubar.addMenu('&Biçim')
        self.word_wrap_action = QAction('Kelime &Kaydırma', self, checkable=True, checked=True)
        self.word_wrap_action.setStatusTip('Satırları pencere genişliğine göre kaydır')
        self.word_wrap_action.triggered.connect(self.toggle_word_wrap)
        format_menu.addAction(self.word_wrap_action)
        self.toggle_word_wrap(True)

        self.choose_font_action = QAction(QIcon.fromTheme("preferences-desktop-font"), '&Yazı Tipi...', self, triggered=self.change_font)
        self.increase_font_action = QAction(QIcon.fromTheme("zoom-in"), "Boyutu &Artır", self, shortcut="Ctrl++", triggered=self.increase_font_size)
        self.decrease_font_action = QAction(QIcon.fromTheme("zoom-out"), "Boyutu &Azalt", self, shortcut="Ctrl+-", triggered=self.decrease_font_size)
        format_menu.addAction(self.choose_font_action)
        format_menu.addAction(self.increase_font_action)
        format_menu.addAction(self.decrease_font_action)

        theme_menu = menubar.addMenu('&Görünüm')
        self.light_theme_action = QAction('Açık Standart Tema', self, checkable=True, triggered=lambda: self.apply_style(LIGHT_CUSTOM_STYLE, "light"))
        self.dark_theme_action = QAction('Koyu Tema', self, checkable=True, triggered=lambda: self.apply_style(DARK_STYLE, "dark"))
        self.sepia_theme_action = QAction('Sepya Kağıt Tema', self, checkable=True, triggered=lambda: self.apply_style(SEPIA_STYLE, "sepia"))
        self.floral_theme_action = QAction('Çiçekli Tema', self, checkable=True, triggered=lambda: self.apply_style(FLORAL_STYLE, "floral"))
        
        theme_menu.addAction(self.light_theme_action)
        theme_menu.addAction(self.dark_theme_action)
        theme_menu.addAction(self.sepia_theme_action)
        theme_menu.addAction(self.floral_theme_action)
        theme_menu.addSeparator()
        self.default_theme_action = QAction('Varsayılan Sistem Teması', self, checkable=True, triggered=lambda: self.apply_style("", "system"))
        theme_menu.addAction(self.default_theme_action)
        
        self.setGeometry(100, 100, 900, 700)
        app_icon = QIcon.fromTheme("accessories-text-editor")
        self.setWindowIcon(app_icon)
        
    
        self.apply_font_settings() 
        self.show()


    def apply_style(self, style_sheet, theme_name):
        self.current_theme_style = style_sheet 
        self.current_theme_name = theme_name   
        QApplication.instance().setStyleSheet(style_sheet)
        
        if theme_name == "light": self.base_window_title = "Açık Not Defteri"
        elif theme_name == "dark": self.base_window_title = "Koyu Not Defteri"
        elif theme_name == "sepia": self.base_window_title = "Sepya Not Defteri"
        elif theme_name == "floral": self.base_window_title = "Çiçekli Not Defteri"
        else: self.base_window_title = "Not Defteri (Sistem)"
        
        self.update_theme_menu_checks()
        self.apply_font_settings()
        self.update_window_title()


    def update_theme_menu_checks(self):
        self.light_theme_action.setChecked(self.current_theme_name == "light")
        self.dark_theme_action.setChecked(self.current_theme_name == "dark")
        self.sepia_theme_action.setChecked(self.current_theme_name == "sepia")
        self.floral_theme_action.setChecked(self.current_theme_name == "floral")
        if hasattr(self, 'default_theme_action'): # Oluşturulduğundan emin ol
            self.default_theme_action.setChecked(self.current_theme_name == "system")


    def apply_font_settings(self):
        current_font = QFont()
        db = QFontDatabase()

        if self.base_font_family and self.base_font_family in db.families():
            current_font.setFamily(self.base_font_family)
        else:
            preferred_families = ["Consolas", "DejaVu Sans Mono", "Menlo", "Courier New"]
            found_preferred = False
            for family in preferred_families:
                if family in db.families():
                    font_info_test = QFontInfo(QFont(family))
                    if font_info_test.fixedPitch():
                        current_font.setFamily(family)
                        self.base_font_family = family 
                        found_preferred = True
                        break
            if not found_preferred:
                current_font.setFamily("monospace") 
                self.base_font_family = current_font.family() 

        current_font.setPointSize(self.base_font_size)
        self.text_area.setFont(current_font)

        status_bar_font = QFont(current_font) 
        status_bar_font.setPointSize(max(8, self.base_font_size - 2))
        if self.statusBar():
             self.statusBar().setFont(status_bar_font)
        
        fm = QFontMetrics(self.text_area.font())
        tab_stop_width = fm.horizontalAdvance('M')
        if tab_stop_width <= 0: tab_stop_width = fm.horizontalAdvance(' ') * 4
        if tab_stop_width <= 0: tab_stop_width = 30
        self.text_area.setTabStopDistance(int(tab_stop_width))

    def change_font(self):
        initial_font = QFont(self.base_font_family, self.base_font_size)
        font, ok = QFontDialog.getFont(initial_font, self, "Yazı Tipi Seç")
        if ok:
            self.base_font_family = font.family()
            self.base_font_size = font.pointSize()
            self.apply_font_settings()
            self.statusBar().showMessage(f"Yazı tipi '{self.base_font_family}', Boyut: {self.base_font_size}pt olarak ayarlandı.")

    def increase_font_size(self):
        if self.base_font_size < 72:
            self.base_font_size += 1
            self.apply_font_settings()
            self.statusBar().showMessage(f"Yazı tipi boyutu: {self.base_font_size}pt")

    def decrease_font_size(self):
        if self.base_font_size > 6:
            self.base_font_size -= 1
            self.apply_font_settings()
            self.statusBar().showMessage(f"Yazı tipi boyutu: {self.base_font_size}pt")

    def update_window_title(self, modified_status_is_irrelevant=None):
        filename_part = os.path.basename(self.current_file) if self.current_file else "Yeni Dosya"
        modified_indicator = "*" if self.text_area.document().isModified() else ""
        self.setWindowTitle(f"{modified_indicator}{filename_part} - {self.base_window_title}")

    def _maybe_save(self):
        if not self.text_area.document().isModified(): return True
        reply = QMessageBox.warning(self, 'Kaydedilmemiş Değişiklikler',
                                      "Mevcut belgede kaydedilmemiş değişiklikler var.\nDeğişiklikleri kaydetmek istiyor musunuz?",
                                      QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel, QMessageBox.Save)
        if reply == QMessageBox.Save: return self.save_file()
        elif reply == QMessageBox.Cancel: return False
        return True

    def new_file(self):
        if not self._maybe_save(): return
        self.text_area.clear(); self.current_file = None
        self.text_area.document().setModified(False); self.update_window_title()
        self.statusBar().showMessage("Yeni dosya oluşturuldu.")

    def open_file(self):
        if not self._maybe_save(): return
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Dosya Aç", "", "Metin Dosyaları (*.txt);;Tüm Dosyalar (*.*)", options=options)
        if file_name:
            try:
                with open(file_name, 'r', encoding='utf-8') as f: self.text_area.setPlainText(f.read())
                self.current_file = file_name; self.text_area.document().setModified(False)
                self.update_window_title(); self.statusBar().showMessage(f"'{os.path.basename(file_name)}' açıldı.")
            except Exception as e:
                QMessageBox.critical(self, "Hata", f"Dosya açılamadı:\n{e}")
                self.current_file = None; self.update_window_title()

    def save_file(self):
        if self.current_file:
            try:
                with open(self.current_file, 'w', encoding='utf-8') as f: f.write(self.text_area.toPlainText())
                self.text_area.document().setModified(False); self.update_window_title()
                self.statusBar().showMessage(f"'{os.path.basename(self.current_file)}' kaydedildi."); return True
            except Exception as e:
                QMessageBox.critical(self, "Hata", f"Dosya kaydedilemedi:\n{e}"); return False
        else: return self.save_as_file()

    def save_as_file(self):
        options = QFileDialog.Options()
        suggested_filename = os.path.basename(self.current_file) if self.current_file else "Adsız.txt"
        file_name, _ = QFileDialog.getSaveFileName(self, "Farklı Kaydet", suggested_filename, "Metin Dosyaları (*.txt);;Tüm Dosyalar (*.*)", options=options)
        if file_name:
            self.current_file = file_name; return self.save_file()
        self.statusBar().showMessage("Farklı kaydetme iptal edildi."); return False

    def toggle_word_wrap(self, checked):
        self.text_area.setLineWrapMode(QTextEdit.WidgetWidth if checked else QTextEdit.NoWrap)
        self.word_wrap_action.setChecked(checked)

    def about_dialog(self):
        year = QDate.currentDate().year()
        QMessageBox.about(self, f"{self.base_window_title} Hakkında",
                          f"<p><b>{self.base_window_title}</b></p>"
                          "<p>PyQt5 ile oluşturulmuş, kişiselleştirilebilir temalı metin düzenleyici.</p>"
                          f"<p>(c) {year}</p>")

    def closeEvent(self, event):
        if self._maybe_save(): event.accept()
        else: event.ignore()

if __name__ == '__main__':
    if hasattr(Qt, 'AA_EnableHighDpiScaling'): QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    if hasattr(Qt, 'AA_UseHighDpiPixmaps'): QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    notepad = ThemedNotepad()
    sys.exit(app.exec_())
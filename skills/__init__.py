from os.path import dirname , basename , isfile , join
import glob


# 取得 _ 套件資料夾 skills 所有檔案名稱
modules = glob.glob( join( dirname( __file__ ) , "*.py" ) )

# 放置功能
skills  = dict()


# 裝飾器 ( Decorator ) : 加入功能
def add_skill( pattern ) :

    def wrapper( func ) :

        skills[pattern] = func

    return wrapper


__all__ = [
            basename(f)[:-3]
            for f in modules
            if isfile( f ) and not f.endswith( '__init__.py' )
          ]


if __name__ == '__main__' :

    # 檢視上面檔案內容
    list = [
             basename(f)[:-3]
             for f in modules
             if isfile(f) and not f.endswith( '__init__.py' )
           ]

    print( list )

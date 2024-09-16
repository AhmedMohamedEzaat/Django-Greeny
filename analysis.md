System :
    - products
    - account [activation,email]
    - orders , track order
    - coupons
    - payments
    - dashboard
    -----------------------------
    - celery , redis
    - cashing
    - optimization
    - django command
    - translation
    - ajax
    - docker
    - deploy [Heroku - aws]
    -----------------------------
    - api
    - docs
--------------------------------------
products :
    - name
    - sku
    - brand          * [name,image]
    - images         *
    - subtitle      
    - description
    - tags           * package
    - price
    - flag [new-sale-festure] dropdown
    - quanitity
    - reviews        * [user_id,product_id,reat[0:5],feedback,datetime]
    - category       * [name,img]


order :
    -status [received,processed,shipped,delivered]
    - user
    - id 
    - total items
    - delivery time
    - order time
    - total
    - sub_total

OrderDetails :
    - order_id
    - product_id 
    - price 
    - quantity
    - total

User :
    - address *
    - name
    - email
    - image
    - phone_number *
------------------------------


     
from django.utils.translation import gettext_lazy as _
GENDER_CHOICES = (
('male',_('Male')),
('female',_('Female'))
)
COLOR_CHOICES = (
('Red', _('Red')),
('Black', _('Black')),
('White', _('White')),
('Grey', _('Grey')),
('Yellow', _('Yellow')),
('Blue', _('Blue')),
('Green', _('Green')),
('Brown', _('Brown')),
('Pink', _('Pink')),
('Purple', _('Purple')),
('Orange', _('Orange')),
)
CITIES_CHOICES = (
    ('Al-Khartoum',_('Al-Khartoum')),
                 ('Bahry',_('Bahry')),
    ('Om-Durman',_('Om-Durman')),
)
COUNTRIES = (
    ('Sudan',_('Sudan')),
    ('Egypt',_('Egypt')),
)
AREA_CHOICES = (
                   ('Om-Baddah',_('om-baddah')),
                   ('Al-Saffyah',_('Al-Saffyah')) ,
                   ('Hay Alarab',_('Hay Alarab')) ,
                   ('Wad Nubawi', _('Wad Nubawi')),
                   ('Al Mawrada', _('Al Mawrada')),
                   ('Hay Al-Omda', _('Hay Al-Omda')),
                   ('Al Mohandsin',_('Al Mohandsin')) ,
                   ('Al Molazmin', _('Al Molazmin')),
                   ('Al Arda', _('Al Arda')),
                   ('Banat gharb', _('Banat gharb')),
                   ('Al Hashmab', _('Al Hashmab')),
                   ('Banat sharg', _('Banat sharg')),
                   ('Hai Al nakhiel', _('Hai Al nakhiel')),
                   ('Emtidad bait Al mal', _('Emtidad bait Al mal')),
                   ('Al Sharfiya', _('Al Sharfiya')),
                   ('Al Jarrafa', _('Al Jarrafa')),
                   ('Al Thawra', _('Al Thawra')),
                   ('Abu Roof',_('Abu Roof')) ,
                   ('Wd Abu Halima', _('Wd Abu Halima')),
                   ('Hay Al-umara Gharb', _('Hay Al-umara Gharb')),
                   ('Bait Al Mal', _('Bait Al Mal')),
                   ('Al Waaha', _('Al Waaha')),
                   ('AL Kabajab', _('AL Kabajab')),
                   ('Hay Al Bosta', _('Hay Al Bosta')),
                   ('Hay Al Mostashfa', _('Hay Al Mostashfa')),
                   ('Al Riyadh', _('Al Riyadh')),
                   ('Al Msalmaa', _('Al Msalmaa')),
                   ('Hay Al-Umara East', _('Hay Al-Umara East')),
                   ('Al Dawha', _('Al Dawha')),
                   ('Sug Al khalifa', _('Sug Al khalifa')),
                   ('Om Bada', _('Om Bada')),
                   ('Alamlaak', _('Alamlaak')),
                   ('Cooper', _('Cooper')),
                   ('Kafouri', _('Kafouri')),
                   ('Bahri Industrial Area', _('Bahri Industrial Area')),
                   ('Al Haj Yousif', _('Al Haj Yousif')),
                   ('Al Sababi', _('Al Sababi')),
                   ('Al Dnagla North', _('Al Dnagla North')),
                   ('Al Dnagla South', _('Al Dnagla South')),
                   ('Hilat Hamad', _('Hilat Hamad')),
                   ('Hilat Khojali', _('Hilat Khojali')),
                   ('Hilat Koko', _('Hilat Koko')),
                   ('Alshabia North', _('Alshabia North')),
                   ('Alshabia South', _('Alshabia South')),
                   ('Almazad', _('Almazad')),
                   ('Almugtaribin', _('Almugtaribin')),
                   ('Almerghania', _('Almerghania')),
                   ('Alsafia', _('Alsafia')),
                   ('Shambat', _('Shambat')),
                   ('AlKhoglab', _('AlKhoglab')),
                   ('Alqadisia', _('Alqadisia')),
                   ('Alhalfaya', _('Alhalfaya')),
                   ('Dardoog', _('Dardoog')),
                   ('Aldroshab', _('Aldroshab')),
                   ('Alkadaro', _('Alkadaro')),
                   ('Alezba', _('Alezba')),
                   ('Alfaki Hashim', _('Alfaki Hashim')),
                   ('Al Gayli', _('Al Gayli')),
                   ('Al Riyadh', _('Al Riyadh')),
                   ('Alamarat', _('Alamarat')),
                   ('Khartoum2', _('Khartoum2')),
                   ('Al-Hilla Al-Jadida', _('Al-Hilla Al-Jadida')),
                   ('Al Diyum East', _('Al Diyum East')),
                   ('khartoum3', _('khartoum3')),
                   ('Burri Almahas', _('Burri Almahas')),
                   ('Nasir Extension', _('Nasir Extension')),
                   ('Al-LaMap', _('Al-LaMap')),
                   ('Burri Al Daraisa', _('Burri Al Daraisa')),
                   ('Burri Alsharif', _('Burri Alsharif')),
                   ('Taha Elmahi', _('Taha Elmahi')),
                   ('Al-Emtidad', _('Al-Emtidad')),
                   ('Saria Residence', _('Saria Residence')),
                   ('Al-Aushara', _('Al-Aushara')),
                   ('Wad-Ageeb', _('Wad-Ageeb')),
                   ('Kalakla Wad Amara', _('Kalakla Wad Amara')),
                   ('Al Diyum West', _('Al Diyum West')),
                   ('Alfirdous East', _('Alfirdous East')),
                   ('Jabra Sharga', _('Jabra Sharga')),
                   ('Al-Jerif West Al-Galaa', _('Al-Jerif West Al-Galaa')),
                   ('Umm Haraz', _('Umm Haraz')),
                   ('Nuzha', _('Nuzha')),
                   ('Wad Husayn', _('Wad Husayn')),
                   ('Al Zohur', _('Al Zohur')),
                   ('Gabra 18', _('Gabra 18')),
                   ('Burri Al Lamab', _('Burri Al Lamab')),
                   ('Abu Dawm', _('Abu Dawm')),
                   ('Garden City', _('Garden City')),
                   ('Gabra 19', _('Gabra 19')),
                   ('Gabra 15', _('Gabra 15')),
                   ('Gabra AlDawha', _('Gabra AlDawha')),
                   ('Gabra 10', _('Gabra 10')),
                   ('Gabra 9', _('Gabra 9')),
)
TYPES_OF_ID = (
    ('Passport',_('Passport')),
    ('National Card',_('National Card')),
    ('National Number',_('National Number'))
)
USERS_ROLES = (
    (1,_('Customer')),
    (2, _('Seller')),
    (3,_('Logistic Driver')),
    (4,_('System User'))
)
DELIVERY_METHOD = (
    ('Flash Delivery',_('Flash Delivery')),
    ('Regular Delivery',_('Regular Delivery')),
)
ORDER_STATUSES = (
('Order Pending',_('Order Pending')),
('Order Placed',_('Order Placed')),
('Order Packaged',_('Order Packaged')),
('Order Out For Delivery',_('Order Out For Delivery')),
('Order Delivered',_('Order Delivered')),
)
PAYMENT_STATUSES = (
    ('Payed',_('Payed')),
    ('UnPayed',_('UnPayed')),
)
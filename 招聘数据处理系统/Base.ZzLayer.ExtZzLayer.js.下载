/*
 *Author Liyao
 *Date 2009-3-17
 *Function ExtZzLayer class
 */

//check the class name , it will be replaced when existed
if ( window.ExtZzLayer ) {
	alert( 'variable ExtZzLayer has been used,it will be replaced with _ExtZzLayer!' );
	window._ExtZzLayer = window.ExtZzLayer;
}

//constructor
window.ExtZzLayer = function( param ) {

	param = param instanceof Object ? param : {};
	
	param.divProps = param.divProps instanceof Object ? param.divProps : {};
	param.divProps.style = param.divProps.style instanceof Object ? param.divProps.style : {};
	param.divProps.style.zIndex = Math.max( param.divProps.style.zIndex || 0 , 1111 );
	
	if ( param.openType != undefined ) {
		this.openType = param.openType;
	}

	this.subBeforeOpen = param.subBeforeOpen || function() {};
	this.subBeforeClose = param.subBeforeClose || function() {};
	
	//filter
	if ( param.filterParam instanceof Object ) {
		if ( !window.ExtZzLayer.prototype.shareFilter ) {
			var fp = param.filterParam;
			//div
			fp.divProps = fp.divProps instanceof Object ? fp.divProps : {};
			fp.divProps.style = fp.divProps.style instanceof Object ? fp.divProps.style : {};
			fp.divProps.style.backgroundColor = fp.divProps.style.backgroundColor || '#000';
			fp.divProps.style.zIndex = param.divProps.style.zIndex - 2;
			fp.divProps.style.filterDepth = fp.divProps.style.filterDepth || 70;
			if ( this.browser.msie ) {
				fp.divProps.style.filter = 'alpha(opacity=' + fp.divProps.style.filterDepth + ')';
			}
			else {
				fp.divProps.style.opacity = fp.divProps.style.filterDepth/100;
			}
			
			//ifr
			fp.createIfr = fp.createIfr != undefined ? fp.createIfr : true;
			if ( fp.createIfr ) {
				if ( this.browser.msie ) {
					fp.ifrProps = { style : { filter: 'alpha(opacity=0)' } };
				}
				else {
					fp.ifrProps = { style : { opacity: 0 } };
				}
				
			}
			else {
				fp.createIfr = false;
				fp.ifrProps = null;
			}

			fp.beforeOpen = function() {
				this.div.style.width = Math.max( document.body.scrollWidth , document.documentElement.scrollWidth ) + 'px';
				this.div.style.height = Math.max( document.body.scrollHeight , document.documentElement.scrollHeight ) + 'px';
			}

			fp.isQuickClose = false;
			window.ExtZzLayer.prototype.shareFilter = new ZzLayer( fp );
		}

		this.filter = window.ExtZzLayer.prototype.shareFilter;
	}

	param.beforeOpen = function() {
		//filter
		if ( this.filter ) {
			this.filter.open();
		}

		switch ( this.openType ) {
			case 1 : this.fallowMouse( arguments[0] , this.div ); break;
			case 2 : this.setCenter( this.div ); break;
		}
		var arg = [];
		for ( var i = 0 ; i < arguments.length ; i++ ) {
			arg.push( arguments[i] );
		}
		this.subBeforeOpen.apply( this , arg );
	}

	param.beforeClose = function() {
		//filter
		if ( this.filter ) {
			this.filter.close();
		}

		var arg = [];
		for ( var i = 0 ; i < arguments.length ; i++ ) {
			arg.push( arguments[i] );
		}
		this.subBeforeClose.apply( this , arg );
	}
	
	//$extends ZzLayer class
	//this.$extends( ZzLayer , param );
	ZzLayer.apply( this , [param] );
}.$extends( ZzLayer );
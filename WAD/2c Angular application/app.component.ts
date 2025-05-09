import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
@Component({
 selector: 'app-root',
 imports: [RouterOutlet],
 templateUrl: './app.component.html',
 styleUrl: './app.component.css'
})
export class AppComponent {
 title = 'Register Form';
 displayname='';
 displayadd='';
 displaycont='';
 displaymail=''
 getValue(name:string, address:string, contact:string, email:string){
 this.displayname=name;
 this.displayadd=address;
 this.displaycont=contact;
 this.displaymail=email;
 }
}
